def searchText(uri):
    global num
    global transNum
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')


    for text in texts:
        print("\n" + text.description)
        synthesize_text(text.description, 'en-US')
        num += 1
        translateStuff(transLang, text.description)
        transNum += 1
