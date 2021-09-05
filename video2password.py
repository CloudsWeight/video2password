'''                  Video 2 Password

Maybe what they say is what they mean?  Let's see.  Add a video clip for your
data and see if it unlocks any doors.  Good luck!

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)

'''

import moviepy.editor as mp

def convert_to_audio(file):

    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(nameAudio+".wav")
    new_audio = (nameAudio+".wav")
    print("Your new file" + new_audio + "is stored in the same folder as this script now.")
    return new_audio

# make sure the file you pass is in the same directory

def get_file():
    print("###############################################################################")
    print("# Convert a video to a password file.                                         #")
    print("# Make sure the file you want to convert is in the same folder as this script.#")
    print("###############################################################################")
    nameAudio = input("What do you want to name the audio file? (Do not add extension):  ")
    data = input("What is the name of your file? (include extension): ")
    return data

if __name__ == '__main__':
    data = get_file()
    convert_to_audio(data)
