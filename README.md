<h1><b>LGMVIP-Python-Task-1</b></h1>

<h2><b>Contents</b></h2>

- [**Introduction**](#introduction)
- [**Details**](#details)
- [**Credits**](#credits)

## **Introduction**
This project is my attempt at Task 1 of the Python Developer internship at LetsGrowMore. The goal is to create a tool which creates GIF images from videos, using Python. The approach taken for this task is creating a GUI application which fulfills all of the desired functions (e.g. adding files, setting parameters and saving files).

## **Details**
* **<u>Project Title:</u>** *Create a GIF Creator using Python*
* **<u>Project Description:</u>** As famous as the gif market has become over these years now, demand for quality gifs is going up. The majority of people use these to communicate with others on social media platforms like WhatsApp, Instagram, etc. We will build a GIF Creator that creates GIFs from images here. In this project, you will be using the `moviepy` Python module for development purposes.
* **<u>Project Submission:</u>** All of the work to be evaluated for this project is found in the `main` folder in the current directory. An explanatory example can also be found in the `notebook` folder in the current directory, in order to aid the reader in better understanding how the contents of the `main` folder work.
* **<u>Libraries Used:</u>** The following libraries were used for the stated purposes:
  - `os`, for handling redundant files;
  - `moviepy`, for extracting GIF images from videos;
  - `PIL`, for image processing, and;
  - `tkinter`, for creating an interactive GUI application carrying out all of the necessary functions.
* **<u>Example Code Snippet:</u>** One example of a code snippet used to build this project is given in the code listing below:
```python
import os
from moviepy.editor import *

def gif_from_video(relative_file_path, subclip, width, speed = 1, fps = 15, resulting_file_name = "result"):
    """
    Generates a GIF image from a single video clip.
    
    Parameters
    ----------
    relative_file_path : str
        A string object representing the relative file path of the video clip
    subclip : tuple
        A tuple object representing the requested start and end timestamps of the video clip (in seconds), respectively
    width : int
        An int object representing the requested width of the resulting GIF image
    speed : int/float, optional
        An int or a float object, representing the requested playback speed of the resulting GIF image. Default : 1
    fps : int, optional
        An int object representing The number of frames per second that the resulting GIF image should have. Default : 15
    resulting_file_name : str, optional
        A string object representing the resulting GIF image's file name (excluding the ".gif" extension declaration). Default : "result"
    Returns
    -------
    moviepy.video.io.VideoFileClip.VideoFileClip
        A moviepy VideoFileClip object representing the resulting GIF image
    """
    clip = VideoFileClip(relative_file_path).subclip(subclip[0], subclip[1]).resize(width = width).fx(vfx.speedx, speed).write_gif(resulting_file_name + ".gif")
    result = VideoFileClip(resulting_file_name + ".gif")
    return result
```

## **Credits**
All of the sources (e.g. videos, images, articles) used to help build this project are cited in the links below:
- https://wave.video/convert/youtube-to-mp4-115
- https://www.youtube.com/shorts/tvDmruktCT4
- https://www.canva.com/design/DAFwSGf12q8/6kt94k-9E9RcZ7a5LhYOcQ/view?utm_content=DAFwSGf12q8&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#11
- https://zulko.github.io/moviepy/
- https://zulko.github.io/blog/2014/01/23/making-animated-gifs-from-video-files-with-python/
- https://www.geeksforgeeks.org/moviepy-getting-sub-clip/
- https://www.geeksforgeeks.org/moviepy-applying-speed-effect-on-video-clip/
- https://www.geeksforgeeks.org/moviepy-saving-video-file-as-gif/
- https://www.geeksforgeeks.org/moviepy-creating-image-clip/
- https://www.youtube.com/watch?v=5qOnzF7RsNA