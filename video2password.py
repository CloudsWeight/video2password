'''                  Video 2 Password

Input a video and hopefully output a working password list!

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)
'''

import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# end of import statements

def banner():
    print("\n###############################################################################")
    print("# Convert a video to a password file.                                         #")
    print("# Make sure the file you want to convert is in the same folder as this script.#")
    print("###############################################################################")

''' COnverting the video to a .WAV audio file'''
def name_file():
    nameAudio = input("What do you want to name the audio file? (Do not add extension):  ")
    return nameAudio

def get_file():
    data = input("What is the name of your file? (include extension): ")
    return data

def convert_to_audio(file, nameAudio):
    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(nameAudio+".wav")
    new_audio = (nameAudio+".wav")
    print("Your new file \"" + new_audio + "\" is stored in the same folder as this script now.")
    print("\n")
    return new_audio

''' Converting the audio to text with SpeechRecognition library from pip and Google recognizer

reference from article below: 
https://www.geeksforgeeks.org/python-speech-recognition-on-large-audio-files/
'''

def write_on_silence(audio):
    song = AudioSegment.from_wav(audio)
    #open file to concantenate and store recognized text
    text = open("recognized.txt", "a")
    # split tracks where silence is 400ms or more, get chunks
    chunks = split_on_silence(song, min_silence_len=400, silence_thresh=-16)
    #create a directory for audio chunks
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass
    #move into the directory to store audio files
    os.chdir('audio_chunks')
    i = 0
    for chunk in chunks:
        chunk_silent= AudioSegment.silent(duration=10)
        #add .5 sec silence to beginning and enf of audio chunk
        audio_chunk = chunk_silent + chunk + chunk_silent
        # export audio chunk and save it in "audio_chunks"
        print("saving chunk{0}.wav".format(i))
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate='192k', format="wav")
        filename = 'chunk'+str(i)+'.wav'
        print("processing chunk "+str(i))
        # get the name of the newly created chunk in the AUDIO_FILE var for future use
        file = filename
        r = sr.Recognizer() #speech recognition object
        #recognize chunk
        '''
        with sr.AudioFile(file) as source:
            # remove if not working right
            r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)
        try:
            rec = r.recognize_google(audio_listened)
            text.write(rec+". ")
        except sr.UnknownValueError:
            print("Error understanding audio")
        except sr.RequestError as e:
            print("Check internet connection")
        '''
        with sr.AudioFile(file) as source:
            audio_listened = r.listen(source)
        try:
            rec = r.recognize_google(audio_listened)
            text.write(rec + ". ")
        except sr.UnknownValueError:
            print("Error understanding audio")
        except sr.RequestError as e:
            print("Check internet connection")

        i += 1 #increment
    os.chdir('..')


'''
def convert_to_text(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
        print("Praying to the Oh Ma Gawds... Om... Om...")
        print("...OM....OM...")
        print(text)
    except:
        print("Thee have been smited!  Or smote! -_-")
        print("Yea the translation to text didn't work.")
'''
def main():
    banner()
    data = get_file()
    name = name_file()
    audio = convert_to_audio(data, name)
    #convert_to_text(audio)
    write_on_silence(audio)


if __name__ == '__main__':
    main()
