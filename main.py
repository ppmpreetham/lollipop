from caption_maker import caption_maker
from video_hex import width_blocks_finder, video_to_rgb, fps

def main():
    FILE_NAME = "tests/BatMobile.mp4"
    print("Hello from lollipop!")
    print(width_blocks_finder(30, 30, 30))
    TOTAL_FPS = fps(FILE_NAME)
    print(f"Detected FPS: {TOTAL_FPS}")
    caption = caption_maker(video_to_rgb(FILE_NAME, pixelHeight=30), fps=TOTAL_FPS)
    NEW_FILE_NAME = FILE_NAME.rsplit('.', 1)[0] + "_caption.dfxp"
    
    with open(NEW_FILE_NAME, 'w', encoding="utf-8") as f:
        f.write(caption)


if __name__ == "__main__":
    main()
