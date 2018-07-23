# Imports the Google Cloud client library
from google.cloud import translate
#Imports the bas64 library to encode images
import base64

# Instantiates a client
client = translate.Client()

print(client.translate('koszula'))







# import io
# import os

# # Imports the Google Cloud client library
# from google.cloud import vision
# from google.cloud.vision import types

# # Instantiates a client
# client = vision.ImageAnnotatorClient()

# # The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'Earth.jpg')

# # Loads the image into memory
# with io.open(file_name, 'rb') as image_file:
#     content = image_file.read()

# image = types.Image(content=content)

# # Performs label detection on the image file
# response = client.label_detection(image=image)
# labels = response.label_annotations

# print('Labels:')
# for label in labels:
#     print(label.description)








# image = open('Earth.jpg', 'rb')
# image_read = image.read()
# image_64_encode = base64.encodestring(image_read)

# print(image_64_encode)

# image_64_decode = base64.decodestring(image_64_encode)
# image_result = open('Earth.jpg', 'wb')
# image_result.write(image_64_decode)