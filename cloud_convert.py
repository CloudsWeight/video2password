'''                Speech to Text Service With IBM Watson
Description:   Using cloud.ibm.com to access cloud Speech to Text-e4 from IBM Watson.
WIll need an [ apikey = ] and a [ url = ] to access resources.
Once '''

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def speech_to_text(speech) -> object: # this will be a string variable of audio filename
    apikey = ''
    url = ''
    authenticator = IAMAuthenticator(apikey)
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url(url)

    with open(speech, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
    text = res['results'][0]['alternatives'][0]['transcript']
    print(res)
    print(text)

