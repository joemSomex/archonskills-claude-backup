#!/usr/bin/env python3
# /// script
# dependencies = ["Pillow>=10", "numpy>=1.24"]
# ///
"""Build and verify a transparent looping GIF from ordered RGBA PNGs."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input-dir', type=Path, required=True)
    ap.add_argument('--pattern', default='*frame*.png')
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--durations', help='one delay for every frame, or comma-separated delays; default 8-frame cheer timing')
    ap.add_argument('--qa-preview', type=Path)
    args = ap.parse_args()
    files = sorted(args.input_dir.glob(args.pattern))
    if len(files) < 2:
        ap.error(f'expected at least 2 ordered PNGs, found {len(files)}: {[x.name for x in files]}')
    if args.durations:
        delays = [int(v) for v in args.durations.split(',')]
        if len(delays) == 1:
            delays *= len(files)
    else:
        delays = [150,150,150,250,150,150,150,250] if len(files) == 8 else [150] * len(files)
    if len(delays) != len(files) or any(v < 20 or v % 10 for v in delays):
        ap.error('durations must be one delay or one per frame, multiples of 10ms and at least 20ms')
    if any(Image.open(p).mode != 'RGBA' for p in files):
        ap.error('all input PNGs must have real RGBA alpha')
    frames = [Image.open(p).convert('RGBA') for p in files]
    size = frames[0].size
    if any(im.size != size for im in frames):
        ap.error('all frames must have identical dimensions')

    samples, red_accents = [], []
    for frame in frames:
        px = np.asarray(frame)[::3, ::3]
        mask = px[:, :, 3] >= 128
        if not mask.any():
            ap.error('a frame is entirely transparent')
        rgb = px[:, :, :3].astype(np.int16)
        samples.append(rgb[mask].astype(np.uint8))
        red = mask & (rgb[:, :, 0] > 65) & (rgb[:, :, 0] > rgb[:, :, 1] * 1.5) & (rgb[:, :, 0] > rgb[:, :, 2] * 1.3)
        if red.any():
            red_accents.append(rgb[red].astype(np.uint8))
    colors = np.concatenate(samples)
    if red_accents:
        colors = np.concatenate((colors, np.tile(np.concatenate(red_accents), (7, 1))))
    pad = (-len(colors)) % 1024
    if pad:
        colors = np.concatenate((colors, colors[:pad]))
    training = Image.fromarray(colors.reshape((-1, 1024, 3)).astype(np.uint8), 'RGB')
    trained = training.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    palette = [0, 0, 0] + trained.getpalette()[:765]
    palette.extend([0] * (768 - len(palette)))
    encoded = []
    for frame in frames:
        px = np.asarray(frame)
        mapped = np.asarray(Image.fromarray(px[:, :, :3], 'RGB').quantize(palette=trained, dither=Image.Dither.NONE), dtype=np.uint8)
        if int(mapped.max()) >= 255:
            raise ValueError('quantizer used index 255; transparency index unavailable')
        indices = np.where(px[:, :, 3] >= 128, mapped.astype(np.uint16) + 1, 0).astype(np.uint8)
        item = Image.fromarray(indices, 'P')
        item.putpalette(palette)
        item.info['transparency'] = 0
        encoded.append(item)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    encoded[0].save(args.output, format='GIF', save_all=True, append_images=encoded[1:], duration=delays, loop=0, transparency=0, disposal=2, optimize=False, background=0)

    gif = Image.open(args.output)
    if gif.format != 'GIF' or gif.n_frames != len(files) or gif.size != size or gif.info.get('loop') != 0:
        raise AssertionError('saved GIF failed format/count/size/loop checks')
    cols = min(4, len(files))
    qa = Image.new('RGB', (size[0] * cols, size[1] * 2 * ((len(files) + cols - 1) // cols))) if args.qa_preview else None
    report = []
    for n, original in enumerate(frames):
        gif.seek(n)
        if gif.info.get('duration') != delays[n]:
            raise AssertionError(f'frame {n+1} duration mismatch')
        decoded = gif.convert('RGBA')
        actual, source = np.asarray(decoded), np.asarray(original)
        opaque = source[:, :, 3] >= 128
        if not np.array_equal(actual[:, :, 3] > 0, opaque):
            raise AssertionError(f'frame {n+1} alpha mask changed')
        if any(actual[y, x, 3] for y, x in ((0, 0), (0, size[0]-1), (size[1]-1, 0), (size[1]-1, size[0]-1))):
            raise AssertionError(f'frame {n+1} has an opaque corner')
        mae = float(np.abs(actual[:, :, :3].astype(np.int16) - source[:, :, :3].astype(np.int16))[opaque].mean())
        if mae >= 20:
            raise AssertionError(f'frame {n+1} palette error too high: {mae:.2f}')
        report.append({'frame': n+1, 'duration_ms': delays[n], 'rgb_mae': round(mae, 2)})
        if qa:
            for j, color in enumerate(('#202020', '#ffffff')):
                background = Image.new('RGBA', size, color)
                background.alpha_composite(decoded)
                qa.paste(background.convert('RGB'), ((n % cols) * size[0], (n // cols) * size[1] * 2 + j * size[1]))
    if qa:
        args.qa_preview.parent.mkdir(parents=True, exist_ok=True)
        qa.save(args.qa_preview, quality=94)
    print(json.dumps({'gif': str(args.output), 'sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(), 'size': list(size), 'frames': report, 'loop': gif.info['loop'], 'qa_preview': str(args.qa_preview) if qa else None}, indent=2))


if __name__ == '__main__':
    main()
