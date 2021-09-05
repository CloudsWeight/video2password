'''                  Video 2 Password

Currently only converts video to .wav audio.  

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)

Author: CloudsWeight
'''

import moviepy.editor as mp

def banner():
    print("\n###############################################################################")
    print("# Convert a video to a password file.                                         #")
    print("# Make sure the file you want to convert is in the same folder as this script.#")
    print("###############################################################################")


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
    return new_audio

# make sure the file you pass is in the same directory



if __name__ == '__main__':
    banner()
    data = get_file()
    name = name_file()
    convert_to_audio(data, name)

