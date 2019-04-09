# Author: Rihards Belinskis ( https://www.github.com/rihardsbelinskis/ )
# Project: r1_S0SAI
# r1_B00K v0.1

# IMPORTING DEPENDENCIES

import pytesseract
import playsound
from gtts import gTTS
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path


pdf_file = 'test.pdf'
pages = convert_from_path(pdf_file, 10) # set an arbitrary page amount
for page in pages:
	page.save('output.jpg', 'JPEG')


im = Image.open("output.jpg") # the second one 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('translated.jpg')
text = pytesseract.image_to_string(Image.open('translated.jpg'))
#print text

speech = gTTS(text)
audio_file = str("b00k.mp3")
speech.save(audio_file)
playsound.playsound(audio_file, True)

