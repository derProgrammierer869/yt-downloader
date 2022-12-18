from pytube import YouTube
import os

def check_path():
    path = r'C:\Users\Yello\Desktop\download'
    if not os.path.exists(path):
        os.mkdir(path)
        print("Download file was created in Desktop.")
    elif os.path.exists(path):
        pass
check_path()
link = input("Please enter the URL of the video:")

yt = YouTube(link)



