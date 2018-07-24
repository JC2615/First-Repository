global num, transNum, userImage, userTranslateLanguage, transLang
num = 0
transNum = 0
transLang = ""

# Imports the Google Cloud client library
from google.cloud import translate

#Imports necessary libraries for google vision API
import io
import os
from google.cloud import vision
from google.cloud.vision import types

userImage = input("Enter and image url: ")
userTranslateLanguage = input("Enter a number that corresponds to the language you'd like the output to be translated to - [1] Spanish, [2] Japanese, [3] French, [4] Italian, [5] German, [6] English: ")

if userTranslateLanguage == "1":
    userTranslateLanguage = "es-US"
elif userTranslateLanguage == "2":
    userTranslateLanguage = "ja-JP"
elif userTranslateLanguage == "3":
    userTranslateLanguage = "fr-FR"
elif userTranslateLanguage == "4":
    userTranslateLanguage = "it-IT"
elif userTranslateLanguage == "5":
    userTranslateLanguage = "de-DE"
elif userTranslateLanguage == "6":
    userTranslateLanguage = "en-US"

transLang = userTranslateLanguage[0:2]


def translateStuff(targetLanguage, text):
    global userTranslateLanguage
    translate_client = translate.Client()
    translation = translate_client.translate(text, target_language = targetLanguage)
    translatedText = translation["translatedText"]
    #print("\n" + translation["input"])
    print("Translation: " + translatedText)
    synthesize_translated_text(translatedText, userTranslateLanguage)

def synthesize_text(text, languageCode):
    global num
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=languageCode,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output' + str(num) + '.mp3', 'wb') as out:
        out.write(response.audio_content)

def synthesize_translated_text(text, languageCode):
    global transNum
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code=languageCode,
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('translated_output' + str(transNum) + '.mp3', 'wb') as out:
        out.write(response.audio_content)

def labelsUrl(uri):
    global num
    global transNum
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print("\n" + label.description)
        synthesize_text(label.description, 'en-US')
        num += 1
        translateStuff(transLang, label.description)
        transNum += 1

def searchFace(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    chances = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(chances[face.anger_likelihood]))
        print('joy: {}'.format(chances[face.joy_likelihood]))
        print('surprise: {}'.format(chances[face.surprise_likelihood]))
        print('sorrow: {}'.format(chances[face.sorrow_likelihood]))
        print('headwear: {}'.format(chances[face.headwear_likelihood]))

def searchLandmark(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    for landmark in landmarks:
        print("The landmark is: " + landmark.description)


def searchLogos(uri):
    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    response = vision_client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print("\n" + logo.description)
        translateStuff(transLang, logo.description)

def searchText(uri):

    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    image = vision.types.Image()
    image.source.image_uri = uri

    # Performs text detection on the image file
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations

    print('Text:')
    for text in texts:
        print("\n" + text.description)
        translateStuff(transLang, text.description)


labelsUrl(userImage)
searchFace(userImage)
searchLandmark(userImage)
searchLogos(userImage)
searchText(userImage)