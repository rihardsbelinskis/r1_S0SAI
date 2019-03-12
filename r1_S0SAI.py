# Author: Rihards Belinskis ( https://www.github.com/rihardsbelinskis/ )
# Project: r1_S0SAI

#-------------------------------------------------------------------------#
# S0SAI is an application, which connects to a selected phone number and  #
# delivers user-set details, in case of emergency. This application is    #
# intended for life-thretening situations, where a person is unable to    #
# speak. The goal is to have a fully automated bot, which delivers user   #
# input to the according person / people.								  #
#-------------------------------------------------------------------------#


# BUGS TO FIX:
#
# 1) If no keyw found, "local variable 'speech' referenced before assignment".
# 2) If an existing keyword is mentioned, "Permission denied".
# 3) Set arbitrary path for any username.
# 4) 

#import array
#import cv2
#import PIL.ImageGrab
#import pytesseract

import numpy as np
import playsound
import os
import stat
import speech_recognition as sr

from PIL import Image
from gtts import gTTS

PATH = "C:/Users/Gebruiker/Desktop/r1_EZPC/"	# Make sure this stays your own path

def audioToText():
	while True:
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('Listening... ')
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
	response_address = "Hospital street 2B, Paisley, United Kingdom"
	response_problem = "The person may be in critical condition and is unable to speak. Please send an ambulance!"
	
	if (not foundKW):
		foundKW = "No keyword has been found."
	elif (foundKW == "'name'"):
		response = response_name
		speech = gTTS(response)
		audio_file = str("response_1.mp3")
		speech.save(audio_file)		# BUG: Permission denied
	elif (foundKW == "'address'"):
		response = response_address
		speech = gTTS(response)
		audio_file = str("response_2.mp3")
		speech.save(audio_file)
	elif (foundKW == "'problem'" | foundKW == "'help'"):
		response = response_problem
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

# FUNCTION: CONNECTED "SPEACH". ADD "if (connected == True): in audioToText()"
#def connectingToAmbulance():
#	connected = False

#	introText = "You are speaking with the R 1 bot. This is an emergency. Please connect me to the ambulance of Hengelo."
#	speech_intro = gTTS(introText)
#	intro_audio_file = str("intro.mp3")
#	speech_intro.save(intro_audio_file)

#	print(introText)
#	playsound.playsound(intro_audio_file, True)

#	connected = True
#	return connected

# FUNCTION: FROM IMAGE TO TEXT
#def textFromImg(PATH):
#	pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
#	saveImg = cv2.imread('save_file.png')

#	kernel = np.ones((1, 1), np.uint8)
#	grayImg = cv2.cvtColor(saveImg, cv2.COLOR_BGR2GRAY)
#	img = cv2.dilate(grayImg, kernel, iterations = 1)
#	img = cv2.erode(img, kernel, iterations = 1)
#	cv2.imwrite(PATH + "removed_noise.png", img)

#	img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#	cv2.imwrite(PATH + "thres.png", img)

#	result = pytesseract.image_to_string(Image.open(PATH + "thres.png"))
#	return result