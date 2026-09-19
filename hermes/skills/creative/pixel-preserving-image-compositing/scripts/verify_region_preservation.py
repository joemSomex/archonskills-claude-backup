#!/usr/bin/env python3
"""Verify that an output changes pixels only inside one rectangle."""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageChops


def parse_rect(value: str) -> tuple[int, int, int, int]:
    parts = value.split(",")
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("rect must be X1,Y1,X2,Y2")
    try:
        rect = tuple(int(part) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("rect values must be integers") from exc
    x1, y1, x2, y2 = rect
    if x1 < 0 or y1 < 0 or x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("rect must have non-negative origin and positive size")
    return rect


def changed_pixels(image: Image.Image) -> int:
    return sum(pixel != (0, 0, 0) for pixel in image.getdata())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--rect", required=True, type=parse_rect)
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGB")
    output = Image.open(args.output).convert("RGB")
    if source.size != output.size:
        print(f"dimension_mismatch source={source.size} output={output.size}")
        return 2

    x1, y1, x2, y2 = args.rect
    width, height = source.size
    if x2 > width or y2 > height:
        print(f"rect_out_of_bounds rect={args.rect} size={source.size}")
        return 2

    diff = ImageChops.difference(source, output)
    outside = Image.new("RGB", source.size)
    outside.paste(diff.crop((0, 0, width, y1)), (0, 0))
    outside.paste(diff.crop((0, y2, width, height)), (0, y2))
    outside.paste(diff.crop((0, y1, x1, y2)), (0, y1))
    outside.paste(diff.crop((x2, y1, width, y2)), (x2, y1))

    outside_count = changed_pixels(outside)
    inside_count = changed_pixels(diff.crop(args.rect))
    print(f"size={source.size}")
    print(f"inside_changed_pixels={inside_count}")
    print(f"outside_changed_pixels={outside_count}")
    return 0 if outside_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
