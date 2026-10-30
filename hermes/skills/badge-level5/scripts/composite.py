# /// script
# dependencies = ["pillow", "numpy", "opencv-python-headless"]
# ///
"""Transfer an E5 texture candidate through one immutable 1000px badge source."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageFilter


def smooth(z: np.ndarray) -> np.ndarray:
    z = np.clip(z, 0, 1)
    return z * z * (3 - 2 * z)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--qa-dir", type=Path, help="Optional dark/light matte previews")
    args = parser.parse_args()

    source_image = Image.open(args.source)
    if source_image.mode != "RGBA" or source_image.size != (1000, 1000):
        parser.error("source must be an original 1000 x 1000 RGBA badge")
    source = np.asarray(source_image).copy()
    weights = np.array([0.2126, 0.7152, 0.0722], np.float32)
    luminance = source[:, :, :3].astype(np.float32) @ weights
    relief = np.asarray(
        Image.fromarray(np.uint8(luminance), "L").filter(ImageFilter.GaussianBlur(1.7)),
        np.float32,
    )
    yy, xx = np.where(source[:, :, 3] > 4)
    if len(xx) == 0:
        parser.error("source alpha contains no badge")
    box = (xx.min(), yy.min(), xx.max(), yy.max())

    candidate_image = Image.open(args.candidate).convert("RGB")
    pic = np.asarray(candidate_image, np.float32)
    if np.max(pic[0, 0]) > 35 or np.max(pic[-1, -1]) > 35:
        parser.error("candidate corners are not dark; inspect/register this candidate manually")
    yy, xx = np.where(pic.max(axis=2) > 35)
    if len(xx) == 0:
        parser.error("candidate has no discernible foreground")
    x0, y0, x1, y1 = xx.min(), yy.min(), xx.max(), yy.max()
    if not (0.55 < (x1 - x0) / pic.shape[1] < 0.98 and
            0.55 < (y1 - y0) / pic.shape[0] < 0.98):
        parser.error("candidate foreground bounding box is implausible; inspect manually")
    scale = min((box[2] - box[0]) / (x1 - x0), (box[3] - box[1]) / (y1 - y0))
    tx = (box[0] + box[2]) / 2 - scale * (x0 + x1) / 2
    ty = (box[1] + box[3]) / 2 - scale * (y0 + y1) / 2
    aligned = cv2.warpAffine(
        pic,
        np.array([[scale, 0, tx], [0, scale, ty]], np.float32),
        (1000, 1000),
        flags=cv2.INTER_LANCZOS4,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0),
    )

    candidate_y = aligned @ weights
    desired = np.interp(
        relief, [0, 35, 65, 95, 135, 180, 255], [4, 12, 26, 48, 72, 125, 205]
    )
    intensity = 0.20 * desired + 0.80 * candidate_y
    hue = np.clip(aligned / np.maximum(candidate_y[:, :, None], 12), 0, 2.6)
    rgb = np.clip(hue * intensity[:, :, None], 0, 255)
    recess = smooth((70 - relief) / 38)
    dark = np.array([20, 24, 15], np.float32) * (intensity / 44)[:, :, None]
    rgb = rgb * (1 - recess[:, :, None] * 0.78) + dark * (recess[:, :, None] * 0.78)

    out = source.copy()
    out[:, :, :3] = np.uint8(np.clip(rgb, 0, 255))
    out[source[:, :, 3] == 0, :3] = source[source[:, :, 3] == 0, :3]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(out, "RGBA").save(args.output)
    check = np.asarray(Image.open(args.output))
    alpha_equal = bool(np.array_equal(check[:, :, 3], source[:, :, 3]))
    transparent_rgb_equal = bool(np.array_equal(
        check[:, :, :3][source[:, :, 3] == 0],
        source[:, :, :3][source[:, :, 3] == 0],
    ))
    if not (alpha_equal and transparent_rgb_equal):
        raise RuntimeError("source alpha/transparent RGB preservation failed")

    if args.qa_dir:
        args.qa_dir.mkdir(parents=True, exist_ok=True)
        for name, background in [("dark", (7, 9, 17, 255)), ("light", (245, 247, 249, 255))]:
            matte = Image.new("RGBA", (1000, 1000), background)
            matte.alpha_composite(Image.open(args.output))
            matte.convert("RGB").save(args.qa_dir / f"qa-{name}.png")

    print(json.dumps({
        "output": str(args.output),
        "size": [1000, 1000],
        "mode": "RGBA",
        "alpha_equal": alpha_equal,
        "transparent_rgb_equal": transparent_rgb_equal,
        "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "candidate_fit": [float(scale), float(tx), float(ty)],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
