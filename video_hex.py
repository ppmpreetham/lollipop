import cv2
import numpy as np

def width_blocks_finder(videoHeight: int = 30, videoWidth: int = 30, heightBlocks: int = 30) -> int:
    return int((videoWidth * heightBlocks) / (videoHeight * 0.55))

def fps(video_path: str) -> int:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("Could not open video.")
    
    fps_value = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return int(fps_value)

def video_to_rgb(video_path, pixelHeight=30):
    cap = cv2.VideoCapture(video_path)
    rgb_frames = []

    if not cap.isOpened():
        raise ValueError("Could not open video.")

    videoHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    videoWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    widthBlocks = width_blocks_finder(videoHeight, videoWidth, pixelHeight)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # MOSAIC VIDEO DOWN
        small = cv2.resize(frame, (widthBlocks, pixelHeight), interpolation=cv2.INTER_LINEAR)

        # Convert to RGB and append to the list
        small_rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
        rgb_frames.append(small_rgb)

        # Show pixelated video
        pixelated = cv2.resize(small, (videoWidth, videoHeight), interpolation=cv2.INTER_NEAREST)
        cv2.imshow('Pixelated', pixelated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print(len(rgb_frames), "frames processed.") # RGB

    # NUMBER OF ROWS
    print("Number of rows:", len(rgb_frames[0]))

    # NUMBER OF COLUMNS
    print("Number of columns:", len(rgb_frames[0][0]))
    return np.array(rgb_frames)