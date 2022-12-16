from pytube import YouTube
from moviepy.editor import *

import os

def getMP3(url):
    video = YouTube(url)
    video = video.streams.filter(only_audio=True).first()
    filename = video.download(output_path='./UPLOAD_FOLDER/')
    clip = AudioFileClip(filename)
    clip.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

    os.remove(filename)
    name = os.path.basename(filename)
    new_file = "./UPLOAD_FOLDER/" + name[:-4] + ".mp3"

    return new_file, video.title




