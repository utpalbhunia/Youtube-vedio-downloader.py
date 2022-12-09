from email.mime import image
from select import select
from tkinter import *
from tkinter import filedialog
from turtle import Screen
from venv import create
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil



# Functions
def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_lable.config(text=path)

def download_file():
    #  to get user path
    get_link = link_field.get() 
    # get selected path 
    user_path = path_lable.cget("text")
    screen.title('Downloading...')
    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()  
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close
    #  Move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!! Download Another file...')

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#  imagelogo
logo_img = PhotoImage(file='youtube-logo-png-2075.png')

#  Size of image
logo_img = logo_img.subsample(3, 3)

canvas.create_image(250, 80 ,image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter the Download Link: ", font=('Arial', 15))

# Add widget to window10-
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Select path for saving the file
path_lable = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn = Button(screen, text="Select", command=select_path)

# Add to window
canvas.create_window(250, 280, window=path_lable)
canvas.create_window(250, 330, window=select_btn)

# Download Button
download_btn = Button(screen, text="Download", command=download_file) 
canvas.create_window(250, 390, window=download_btn)


screen.mainloop() 