# Author: Rihards Belinskis ( https://www.github.com/rihardsbelinskis/ )
# Project: r1_S0SAI


# IMPORTING DEPENDENCIES

#import array
#import cv2
#import PIL.ImageGrab
#import pytesseract
#import stat
#from PIL import Image

import numpy as np
import playsound
import os
import speech_recognition as sr
from gtts import gTTS

# GLOBAL VARIABLES

PATH = os.path.join(os.path.expanduser('~'), 'Desktop', 'r1_S0SAI')

def audioToText():
	while True:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('\nListening... ')
			audio = r.listen(source)
			try:
				inputText = r.recognize_google(audio)
				print('Input: {}'.format(inputText))
				return inputText
			except:
				print('No command has been input.')

def keywordFinder(inputText):
	keywords = ['help', 'address', 'Name', 'name', 
			 'first name', 'situation', 'happened', 'problem']
	foundKW = [keyword for keyword in keywords if keyword in inputText]
	if (not foundKW): 	# BUG: if no keyw, it gets confused
		foundKW = "No keyword has been found."
	else:
		foundKW = str(foundKW)[1:-1]
		print("Found keyword: ", foundKW)
		return foundKW

def responseSelector(foundKW):
	response = ''
	response_name = "Bobby"
	response_address = "Troll street 120A, Paisley, United Kingdom"
	response_problem = "The person may be in critical condition and is unable to speak. Please send an ambulance!"

	if not (foundKW):
		response = "No keyword has been found."
		print("Response: ",response)
		speech = gTTS(response)
	elif (foundKW == "'name'"):
		response = response_name
		print("Response: ",response)
		speech = gTTS(response)
		audio_file = str("response_1.mp3")
		speech.save(audio_file)		# BUG: Permission denied
	elif (foundKW == "'address'"):
		response = response_address
		print("Response: ",response)
		speech = gTTS(response)
		audio_file = str("response_2.mp3")
		speech.save(audio_file)
	elif (foundKW == "'problem'"):
		response = response_problem
		print("Response:",response)
		speech = gTTS(response)
		audio_file = str("response_3.mp3")
		speech.save(audio_file)
	return (speech, audio_file)

def responseToSpeech(speech, audio_file):
	print("Response: ", speech)
	playsound.playsound(audio_file, True)

if __name__ == '__main__':
	while True:
		inputText = audioToText()
		foundKW = keywordFinder(inputText)
		[speech, audio_file] = responseSelector(foundKW)
		output = responseToSpeech(speech, audio_file)
		os.remove(audio_file)
