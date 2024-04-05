# Source : 
#    https://stackoverflow.com/questions/33448759/python-converting-video-to-audio

import moviepy.editor as mp
clip = mp.VideoFileClip("PATH/TO/VIDEO.mp4") 
clip.audio.write_audiofile("PATH/TO/AUDIO.mp3")