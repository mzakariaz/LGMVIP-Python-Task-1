# Import packages
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from moviepy.editor import *

# Define GIF conversion function
def gif_from_video(file_path, subclip, width, speed = 1, fps = 15, resulting_file_name = "result"):
    """
    Generates a GIF image from a single video clip.
    
    Parameters
    ----------
    file_path : str
        A string object representing the file path of the video clip
    subclip : tuple
        A tuple object representing the requested start and end timestamps of the video clip (in seconds), respectively
    width : intG
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
    clip = VideoFileClip(file_path)
    clip = clip.subclip(subclip[0], subclip[1])
    clip = clip.resize(width = width)
    clip = clip.fx(vfx.speedx, speed)
    current_file_path = os.path.abspath(__file__)
    current_directory_path = current_file_path[:current_file_path.rindex("\\") + 1].replace("\\", "/")
    resulting_file_path = current_directory_path + resulting_file_name + ".gif"
    clip = clip.write_gif(resulting_file_path)
    result = VideoFileClip(resulting_file_path)
    return result

# Define video submission button function
def video_submission():
   """
   An auxiliary function used to browse files and call the main function (gif_from_video), in order to convert video files to GIF images.

   Parameters
   ----------
   None

   Returns
   -------
   None
   """
   file_path = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = [("All Files", "*.*")])
   start_second = int(start_second_entry.get())
   end_second = int(end_second_entry.get())
   subclip = (start_second, end_second)
   width = int(width_entry.get())
   speed = float(speed_entry.get())
   fps = int(fps_entry.get())
   resulting_file_name = resulting_file_name_entry.get()
   gif_from_video(file_path, subclip, width, speed, fps, resulting_file_name)

# Initialise the application
window = tk.Tk()
window.title("GIF Creator")
frame = tk.Frame(window)
frame.pack()

# Initialise the How to Use frame and its content
how_to_use = tk.LabelFrame(frame, text = "How to Use")
how_to_use.grid(row = 0, column = 0, padx = 10, pady = 10)
instructions = """Welcome! This application is an elementary GIF creator that extracts dynamic GIF images from videos. Here is a basic explanation of all of the parameters
that can be chosen by the user:
    - Beginning second: The second number in the video at which the GIF image should begin;
    - Ending second: The second number in the video at which the GIF image should end (not that it must exceed the beginning second and cannot 
    exceed the video length in seconds);
    - Width (in pixels): The width, in pixels, that the GIF image should have (between 10 and 5000, inclusive);
    - Speed: The speed at which the GIF should play (between 0.1 and 50, inclusive);
    - Frames per second: The number of frames per second at which the GIF image should play (between 5 and 120 inclusive), and;
    - Resulting GIF name: The name which the resulting GIF image should have (excluding the ".gif" extension declaration).
Once the parameters have been entered correctly, the GIF image will be generated in the same directory where the script for this application is located.
In order to avoid unexpected errors, make sure that ALL OF THE GIF PARAMETERS ARE ENTERED CORRECTLY! Happy GIF creating!"""

# Add the label for the instructions
instruction_label = tk.Label(how_to_use, text = instructions, justify = "left")
instruction_label.grid(row = 0, column = 0)

# Initialise the GIF Parameters frame
gif_parameters = tk.LabelFrame(frame, text = "GIF Parameters")
gif_parameters.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")

# Add the labels and entries for the GIF parameters
start_second_label = tk.Label(gif_parameters, text = "Beginning second:")
start_second_label.grid(row = 0, column = 0)
start_second_entry = tk.Entry(gif_parameters)
start_second_entry.grid(row = 0, column = 1)

end_second_label = tk.Label(gif_parameters, text = "Ending second:")
end_second_label.grid(row = 1, column = 0)
end_second_entry = tk.Entry(gif_parameters)
end_second_entry.grid(row = 1, column = 1)

width_label = tk.Label(gif_parameters, text = "Width (in pixels):")
width_label.grid(row = 2, column = 0)
width_entry = ttk.Spinbox(gif_parameters, from_ = 10, to = 5000)
width_entry.grid(row = 2, column = 1)

speed_label = tk.Label(gif_parameters, text = "Speed:")
speed_label.grid(row = 0, column = 2)
speed_entry = ttk.Spinbox(gif_parameters, from_ = 0.1, to = 50.0)
speed_entry.grid(row = 0, column = 3)

fps_label = tk.Label(gif_parameters, text = "Frames per second:")
fps_label.grid(row = 1, column = 2)
fps_entry = ttk.Spinbox(gif_parameters, from_ = 5, to = 120)
fps_entry.grid(row = 1, column = 3)

resulting_file_name_label = tk.Label(gif_parameters, text = "Resulting GIF name:")
resulting_file_name_label.grid(row = 2, column = 2)
resulting_file_name_entry = tk.Entry(gif_parameters)
resulting_file_name_entry.grid(row = 2, column = 3)

# Initialise the video submission frame
video_submission_frame = tk.LabelFrame(frame, text = "Submit Video")
video_submission_frame.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")

# Add a video submission button
video_submission_button = tk.Button(video_submission_frame, text = "Submit Your Video Here", command = video_submission)
video_submission_button.grid(row = 0, column = 0)

# Add spaces between the labels and their entries
for label_frame in [how_to_use, gif_parameters, video_submission_frame]:
    for widget in label_frame.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)

# Make the window impossible to resize
window.resizable(False, False)

# Make the window run indefinitely until the user manually closes it.
window.mainloop()
