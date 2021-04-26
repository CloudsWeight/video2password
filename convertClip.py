''' module to convert video audio to a wav file, read moviepy docs '''
import moviepy.editor as mp
def convert(file):
    global new_audio
    nameAudio = input("What do you want to name the audio file? (Do not add extension):")
    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(nameAudio+".wav")
    new_audio = (nameAudio+".wav")
