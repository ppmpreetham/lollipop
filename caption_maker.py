from video_hex import video_to_rgb
import numpy as np

def appendColor(hex: str, count: int) -> str:
    chars = "█" * count
    return f"&lt;font color=&quot;#{hex}&quot;&gt;{chars}&lt;/font&gt;"

def makeRow(start: float, dur: float, hex_list: list[str]) -> str:
    if not hex_list:
        return ""

    row = [f'<text start="{start}" dur="{dur}">']

    prev = hex_list[0]
    count = 1

    for curr in hex_list[1:]:
        if curr == prev:
            count += 1
        else:
            row.append(appendColor(prev, count))
            prev = curr
            count = 1
    row.append(appendColor(prev, count))

    row.append("</text>")
    return ''.join(row)


# hexes = [
#     "464037", "433C33", "413B32", "403930", "41392F", "40382D",
#     "3E372E", "3A352F", "373430", "343330", "363737", "363838"
# ]
# print(makeRow(0.0, 0.083, hexes))

def caption_maker(rgb_frames):
    caption = []
    caption.append("<?xml version=\"1.0\" encoding=\"utf-8\" ?>")
    caption.append("<transcript>")
    caption.append("</transcript>")
