from pytube import YouTube
import os
import time

path = r'C:\Users\Yello\Desktop\YT_Download'

def download():
    link = input("Please enter the URL of the video:")
    yt = YouTube(link)
    yn = input('Download' + yt.title + '? (y/n)')
    if yn == 'y':
        #yt.set_filename(yt.title)  --download the repo https://github.com/NFicano/pytube
        d_video = yt.streams.first()
        d_video.download(path)
        
    elif yn == 'n':
        print('Download cancelled.')
        time.sleep(3)
        exit()


def check_path():
    if not os.path.exists(path):
        os.mkdir(path)
        download()
        print("Download file was created in Desktop.")
    elif os.path.exists(path):
        download()
check_path()

# Link: https://www.youtube.com/watch?v=rDMAT1a5bPM&t=227s

#make download progress bar
