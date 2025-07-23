from video_hex import width_blocks_finder, video_to_rgb

def main():
    print("Hello from lollipop!")
    print(width_blocks_finder(30, 30, 30))
    print(video_to_rgb("tests/BatMobile.mp4", pixelHeight=30))


if __name__ == "__main__":
    main()
