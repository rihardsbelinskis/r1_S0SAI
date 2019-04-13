# Author: Rihards Belinskis ( https://www.github.com/rihardsbelinskis/ )
# Project: r1_S0SAI
# r1_B00K v0.3

# IMPORTING DEPENDENCIES

import pytesseract
import playsound
import os
from gtts import gTTS
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path

# Initializing the pdf_file, correcting the generated mp3 title
pdf_file = 'test.pdf'
title_end = pdf_file.index('.')
title = pdf_file[:title_end]

def pdfTextExtractor():
    # Converting the pdf file to a jpeg
    pages = convert_from_path(pdf_file, 500) # 500 for correct zoom
    for page in pages:
            page.save('output.jpg', 'JPEG')

    # Image operations
    im = Image.open("output.jpg")
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('translated.jpg')
    text = pytesseract.image_to_string(Image.open('translated.jpg'))
    print(text) # debugging
    return text

def mp3generator(text):
    # Generating and playing the audiobook mp3
    speech = gTTS(text)
    audio_file = str(title+"_audiob00k.mp3")
    speech.save(audio_file)

    # Playing the .mp3 file 
    #playsound.playsound(audio_file, True)

if __name__ == '__main__':
    # Main loop
    text = pdfTextExtractor()
    mp3generator(text)

    # Removing temporary files
    os.remove('translated.jpg')
    os.remove('output.jpg')


