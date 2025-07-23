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
#     "464037", "464037", "413B32", "403930", "41392F", "40382D",
#     "3E372E", "3A352F", "373430", "343330", "363737", "363838"
# ]
# print(makeRow(0.0, 0.083, hexes))

def rgb_to_hex_list(rgb_frame: np.ndarray) -> list[str]:
    h, w, _ = rgb_frame.shape
    flattened = rgb_frame.reshape(h * w, 3)
    return ['{:02X}{:02X}{:02X}'.format(r, g, b) for r, g, b in flattened]

def caption_maker(rgb_frames: np.array, fps: float = 12.0) -> str:
    caption = []
    caption.append("<?xml version=\"1.0\" encoding=\"utf-8\" ?>")
    caption.append("<transcript>")
    
    frame_duration = 1 / fps

    for i, frame in enumerate(rgb_frames):
        start = i * frame_duration
        hex_list = rgb_to_hex_list(frame)
        caption.append(makeRow(start, frame_duration, hex_list))


    caption.append("</transcript>")
    return ''.join(caption)
