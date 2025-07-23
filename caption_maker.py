from video_hex import video_to_rgb
import numpy as np

def appendColor(hex):
    return f"&lt;font color=&quot;#{hex}&quot;&gt;█&lt;/font&gt;"

def makeRow(start: float, dur: float, hex_list: list[str]) -> str:
    row = [f'<text start="{start}" dur="{dur}">']
    row.append(''.join(appendColor(h) for h in hex_list))
    row.append('</text>')
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
