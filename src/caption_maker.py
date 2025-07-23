import numpy as np

def makeSpan(hex: str, count: int) -> str:
    return f'<span style="color:#{hex}">{"█" * count}</span>'

def makeRowParagraph(start: float, dur: float, hex_row: list[str], row_idx: int) -> str:
    if not hex_row:
        return ""
    
    parts = [f'<p begin="{start:.3f}s" end="{start + dur:.3f}s" region="row{row_idx}">']
    prev = hex_row[0]
    count = 1

    for curr in hex_row[1:]:
        if curr == prev:
            count += 1
        else:
            parts.append(makeSpan(prev, count))
            prev = curr
            count = 1
    parts.append(makeSpan(prev, count))
    parts.append("</p>")
    return ''.join(parts)

def rgb_to_hex_rows(rgb_frame: np.ndarray) -> list[list[str]]:
    return [
        ['{:02X}{:02X}{:02X}'.format(*rgb_frame[y, x]) for x in range(rgb_frame.shape[1])]
        for y in range(rgb_frame.shape[0])
    ]

def generate_regions(num_rows: int) -> str:
    region_template = '<region xml:id="row{0}" tts:origin="0% {1:.2f}%" tts:extent="100% {2:.2f}%" />'
    extent = 100.0 / num_rows
    return '\n'.join(
        region_template.format(i, i * extent, extent)
        for i in range(num_rows)
    )

def caption_maker(rgb_frames: np.ndarray, fps: float = 12.0) -> str:
    frame_duration = 1 / fps
    num_rows = rgb_frames[0].shape[0]

    header = f'''<?xml version="1.0" encoding="utf-8"?>
<tt xmlns="http://www.w3.org/ns/ttml"
    xmlns:tts="http://www.w3.org/ns/ttml#styling"
    xml:lang="en">
  <head>
    <layout>
{generate_regions(num_rows)}
    </layout>
  </head>
  <body>
    <div>'''

    footer = '''
    </div>
  </body>
</tt>'''

    body = []
    for i, frame in enumerate(rgb_frames):
        start = i * frame_duration
        hex_rows = rgb_to_hex_rows(frame)
        for row_idx, row in enumerate(hex_rows):
            body.append(makeRowParagraph(start, frame_duration, row, row_idx))

    return header + '\n'.join(body) + footer
