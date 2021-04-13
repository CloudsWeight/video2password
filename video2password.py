'''Video to Password
Maybe what they say is what they mean?  Let's see.  Add a video clip for your
data and see if it unlocks any doors.  Good luck!

Details: Import moviepy and SpeechRecognition to pull that data.  Translate the
video into audio files, then translate the audio into text, then output the
results to a custom file.

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)
    Audio Formats:
        MP3
        AAC
        WMA
        AC3 (Dolby Digital)
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
# if you need to test global results un-comment the print()s below
# print(your_file)
###############################################################################

# convert your_file into .wav format
def convertCLip():
    global nameTxt
    global nameAudio
    nameAudio = input("What do you want to name the audio file? (Do not add extension):")
    # your_file  = str(your_file)
    clip = mp.VideoFileClip(your_file)
    new_audio = clip.audio.write_audiofile(nameAudio+".wav")

convertCLip()
###############################################################################

# function to
def audioText():
    global newTxt
    newTxt = input("What do you want to name the text file? (Do not add extension):")
    newTxt = newTxt+".txt"

audioText()
print(newTxt)

# NOTES
# currently working on pulling text from wav file
