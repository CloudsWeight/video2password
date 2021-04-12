''' Video to Password
Maybe what they say is what they mean?  Let's see?  Add a video clip for your
data and see if your output unlocks any doors.  Good luck!


Details: Import moviepy and SpeechRecognition to pull that data.  Translate the
video into audio files, then translate the audio into text, then output to custom file.
Author: Nick Sepe

'''

import speech_recognition as sr
import moviepy.editor as mp

# create a function to read the file and make sure it's a valid format
def theFile():
    your_file = input("Copy paste your video file:")
    fileLength = []
    for i in your_file:
        fileLength.append(i)
    n = len(fileLength)
    print(fileLength[n-4:n])
theFile()
#clip = mp.VideoFileClip(your_file)
#clip.audio.write_audiofile(r"converted.wav")
