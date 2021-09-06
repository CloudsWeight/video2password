'''                  Video 2 Password

Desscription:  Program takes a video, converts it to .mp3. 
Then translates the speech in the .mp3 to a text list, currently.  More plans in the future.
This is a working version that will need an [ apikey = ] and a [ url = ] to access resources.

    Acceptable Video Formats:
        MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
        3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
        OGG (ogg, oga, ogv, ogx)
        WMV (wmv, wma, asf*)
        
Author: Nick Sepe

'''
import moviepy.editor as mp #convert_to_audio dep
#from cloud_convert import speech_to_text as stt
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#import os

def convert_to_audio(file, name_of_audio): # Use moviepy to convert audio
    clip = mp.VideoFileClip(file)
    clip.audio.write_audiofile(name_of_audio+".mp3")
    speech = (name_of_audio+".mp3")
    print("Your new file \"" + speech + "\" is stored in the same folder as this script now.")
    return str(speech)

#def convert_to_speech(speech): # IBM Watson Text to Speech function
    #stt(speech)

def speech_to_text(speech) -> object: # this will be a string variable of audio filename
    print("Converting speech to text now....")
    # apikey from the cloud.ibm.com website, use your individual apikey
    apikey = ''
    # url from the cloud.ibm.com website , use your individual url
    url = ''
    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open(speech, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
    text=[]
    for result in res['results']:
        text.append(result['alternatives'][0]['transcript'])
    print(text)
    
def banner(): # hello
    print("################################################################################")
    print("#       [  Video2Password: Convert a video to a password file.  ]              #")
    print("# Make sure the file you want to convert is in the same folder as this script. #")
    print("################################################################################")

def get_file(): # store the name of the file in the folder
    print("****************************************************************************")
    print("* Use file extension (example.mp4).  File must be in same folder as script.*")
    data = input("* What is the name of the video file to convert?: ")
    return data

def name_file():
    nameAudio = input("What do you want to name the audio file?:  ")
    return nameAudio

def main():
    banner()
    data = get_file()
    name = name_file()
    speech = convert_to_audio(data, name)
    speech_to_text(speech)

if __name__ == '__main__':
    main()
