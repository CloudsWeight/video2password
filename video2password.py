'''                  Video to Password

Maybe what they say is what they mean?  Let's see.  Add a video clip for your
data and see if it unlocks any doors.  Good luck!

Details: Import moviepy and SpeechRecognition to pull that data.  Translate the
video into audio files, then translate the audio into text, then output the
text to a custom file.

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)
        
License: Git The Unlicense  
Author: Nick Sepe
'''
###############################################################################
# imports
import speech_recognition as sr
import moviepy.editor as mp
import os
###############################################################################
# read the file (TO DO:make sure it's a valid format)

def theFile():
    # your_file will be what we pass to our main function
    global your_file
    your_file = input("Copy paste your video file:")
    # below is for valid format checks, TO DO!
    # filesplit = os.path.splitext(your_file)
    # fileIs = filesplit[1]

theFile()
###############################################################################
# if you need to test global results for your_file un-comment the print() below
# print(your_file)
###############################################################################
# convert your_file into .wav format

def convertCLip():
    global new_audio
    nameAudio = input("What do you want to name the audio file? (Do not add extension):")
    # your_file  = str(your_file)
    clip = mp.VideoFileClip(your_file)
    clip.audio.write_audiofile(nameAudio+".wav")
    new_audio = (nameAudio+".wav")

convertCLip()
###############################################################################
# if you need to test global results for new_audio un-comment the print() below
# print(new_audio)
###############################################################################
# use pydub to break up large audio into smaller sections based on silence in the data





# this function is defunct unless the video is very short, here as an artifact 
###############################################################################
# function to convert wav to text, only works for small files :-(
#def audioText():
#    global newTxt
#    newTxt = input("What do you want to name the text file? (Do not add extension):")
#    newTxt = newTxt+".txt"
#    #initialize the SpeechRecognition recognizer
#    r = sr.Recognizer()
#    with sr.AudioFile(new_audio) as source:
#       #load audio
#        audioRead = r.record(source)
        # conversion is happening man!
#        text = r.recognize_google(audioRead)
#        print(text)
#audioText()
