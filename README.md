# Lollipop
An Open Source app which converts videos to subtitles/captions. This is specifically aimed for videos for YouTube, but can be used for any video.

## How does it work?
The `█` character is used to represent a pixel in the video, with a ratio of `0.55 : 1`.
For a video, the max blocks for height one can have is n `(preferably 30)` while the width can be as large as needed. It's calculated as follows:

```
$$
\text{width\_blocks} = \frac{W \cdot n}{0.55 \cdot \text{screen\_height}}
$$
```
where `screen_height` is the height of the screen in pixels, and `n` is the number of blocks you want to use for the height of the video.
The app reads the video file, processes each frame, and generates a text representation of the video content using the `█` character to represent pixels. The output can be used as subtitles or captions for the video.
