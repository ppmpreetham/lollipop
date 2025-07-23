import numpy as np
from video_hex import fps

def appendColor(hex: str, count: int) -> str:
    return f"&lt;font color=&quot;#{hex}&quot;&gt;{'█' * count}&lt;/font&gt;"

def makeTextTag(start: float, dur: float, hex_row: list[str]) -> str:
    if not hex_row:
        return ""

    parts = [f'<text start="{start:.3f}" dur="{dur:.3f}">']
    prev = hex_row[0]
    count = 1

    for curr in hex_row[1:]:
        if curr == prev:
            count += 1
        else:
            parts.append(appendColor(prev, count))
            prev = curr
            count = 1
    parts.append(appendColor(prev, count))
    parts.append("</text>")
    return ''.join(parts)

def rgb_to_hex_rows(rgb_frame: np.ndarray) -> list[list[str]]:
    return [
        ['{:02X}{:02X}{:02X}'.format(*rgb_frame[y, x]) for x in range(rgb_frame.shape[1])]
        for y in range(rgb_frame.shape[0])
    ]

def caption_maker(rgb_frames: np.ndarray, fps: float = 12.0) -> str:
    frame_duration = 1 / fps
    caption = ['<?xml version="1.0" encoding="utf-8" ?>', '<transcript>']

    for i, frame in enumerate(rgb_frames):
        start = i * frame_duration
        hex_rows = rgb_to_hex_rows(frame)
        for row in hex_rows:
            caption.append(makeTextTag(start, frame_duration, row))

    caption.append('</transcript>')
    return ''.join(caption)
