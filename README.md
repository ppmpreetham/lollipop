# Lollipop
An Open Source Script that converts videos to subtitles/captions. This is specifically aimed for videos for YouTube, but can be used for any video.
Inspired by [this video](https://www.youtube.com/watch?v=LPrTdT8HedU) by Ubonga.

| Before | After |
|--------|-------|
| ![Before](README/before.png) | ![After](README/after.png) |

> [!IMPORTANT]  
> Colors don't work yet for `YouTube`, but the position of the subtitles is correct.
 
## How does it work?
The `█` character is used to represent a pixel in the video, with a ratio of `0.55 : 1` for the [Roboto](https://fonts.google.com/specimen/Roboto) font that YouTube uses on it's browser.

For a video, the max blocks for height one can have is n `(preferably 30)` while the width can be as large as needed. It's calculated as follows:

$$
\text{widthBlocks} = \frac{W \cdot n}{0.55 \cdot \text{screenHeight}}
$$

where `screenHeight` is the height of the screen in pixels, and `n` is the number of blocks you want to use for the height of the video.
The app reads the video file, processes each frame, and generates a text representation of the video content using the `█` character to represent pixels. The output can be used as subtitles or captions for the video.

The `dfxp` file format is used to store the generated subtitles. It not only stores the subtitles, but also the `position` and `color` of the subtitles. 
- `position` is calculated based on the width and height of the video
- `color` is determined by the average color of the pixels in each block through mosaicization

## Usage
To use Lollipop, follow these steps:

1. Install the required dependencies.
   ```bash
   uv install -r requirements.txt
   ```
   Ensure you have Python 3.8 or higher installed.

2. Run the application with the video file as input.
3. Configure the output settings (e.g., subtitle format, resolution).
4. Start the conversion process.
5. Retrieve the generated subtitles from the output directory.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.
But the current issues we're facing are:

[ ] Right format of the dfxp file to support the color
[ ] Improve video processing speed
