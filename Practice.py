
# Imports the Google Cloud client library
from google.cloud import translate

#Imports the bas64 library to encode images
import base64

#Imports necessary libraries for google vision API
import io
import os
from google.cloud import vision
from google.cloud.vision import types

from google.cloud.vision_v1 import ImageAnnotatorClient

# Instantiates a client
translate_client = translate.Client()

# Instantiates a client
vision_client = vision.ImageAnnotatorClient()

global image_client
image_client = ImageAnnotatorClient()
# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'Earth.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = vision_client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
    translation = translate_client.translate(label.description, target_language = 'es')
    translatedText = translation["translatedText"]
    print("\n" + translation["input"])
    print("Translation: " + translatedText)


def detect_labels_url(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        print(label.description)

detect_labels_url("https://www.what-dog.net/Images/faces2/scroll0015.jpg")


def baseEncode(theImage):
    image = open(theImage, 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)

    print(image_64_encode)

    image_64_decode = base64.decodestring(image_64_encode)
    image_result = open('Earth.jpg', 'wb')
    image_result.write(image_64_decode)

