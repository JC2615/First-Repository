import io
import os
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate
import sys
#print(sys.stdout.encoding)


def searchLabel(picture):

    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        picture)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = vision_client.label_detection(image=image)
    labels = response.label_annotations

    print(len(labels))

    print('Labels:')
    for label in labels:
        translation = translate_client.translate(label.description, target_language = 'es')
        translatedText = translation["translatedText"]
        print("\n" + translation["input"])
        print("Translation: " + translatedText)







def searchLogos(picture):
    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        picture)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = vision_client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')



    for logo in logos:
        translation = translate_client.translate(logo.description, target_language = 'es')
        translatedText = translation["translatedText"]
        print("\n" + translation["input"])
        print("Translation: " + translatedText)


def searchText(picture):

    # Instantiates a client
    translate_client = translate.Client()

    # Instantiates a client
    vision_client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        picture)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs text detection on the image file
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations

    print('Labels:')
    for text in texts:
        translation = translate_client.translate(text.description, target_language = 'es')
        translatedText = translation["translatedText"]
        print("\n" + translation["input"])
        print("Translation: " + translatedText)


def searchLandmark(picture):
    vision_client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        picture)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = vision_client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    for landmark in landmarks:
        print("The landmark is: " + landmark.description)




def searchFace(picture):
    client = vision.ImageAnnotatorClient()

    file_name = os.path.join(
        os.path.dirname(__file__),
        picture)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

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


def final(picture):
    # searchLabel(picture)
    # searchLogos(picture)
    # searchText(picture)
    #searchLandmark(picture)
    searchFace(picture)
    #detect_face(picture)

final("man.jpg")


