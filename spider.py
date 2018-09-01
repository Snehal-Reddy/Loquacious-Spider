import tkinter as tk
from tkinter import ttk
import os
import time
import webbrowser
import json
import requests
import ctypes
import youtube_dl
import random
import urllib
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen
import speech_recognition as sr
import requests
import pyttsx3
import sys
import threading
from datetime import datetime
import errno
import subprocess
import csv
import regex

requests.packages.urllib3.disable_warnings()
try:
		_create_unverified_https_context=ssl._create_unverified_context
except 'AttributeError':
		pass
else:
		ssl._create_default_https_context=_create_unverified_https_context

home_directory = os.environ['HOME']

speak = pyttsx3.init()

def voice (frame, put,link):

	#news
	if any('news' in  put):
		speak.say('Which news agency would you prefer today ? BBC , ESPN or al jazeera ? ')
		recogniser = sr.Recognizer()
		with sr.Microphone() as source:
			speak.say('Hey I am Listening ')
			speak.runAndWait()
			audio1 = recogniser.listen(source)
		try:
			put1=recogniser.recognize_google(audio1)
			put1=put1.lower()
			put1 = put1.strip()
			link1=put.split()
			say1 = '+'.join(link1)
			if link1[1] == "al" and link[2] == "jazeera":
				say1 += "-english"
			elif link1[1] == "bbc":
				say1 += "-news"
			elif link1[1] == "espn" and link[2] == "cric":
				say1 += "-info"
			url1 = ('https://newsapi.org/v1/articles?source=' + say1 + '&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
			newsresponce = requests.get(url1)
			newsjson = newsresponce.json()
			speak.say('My friends from ' + say1 + ' report this')
			speak.runAndWait()
			frame.displayText('  ====='+ say1.upper() +'===== \n')
			i = 1
			for item in newsjson['articles']:
				frame.displayText(str(i) + '. ' + item['title'] + '\n')
				frame.displayText(item['description'] + '\n')
				i += 1
		except sr.UnknownValueError:
			speak.say("Could not understand audio")
		except sr.RequestError as e:
			speak.say("Could not request results")
		except:
			speak.say('Unable to retrieve data!')

	#weather
	if any('weather' in put):
		APIKEY = '1410da5b0f0ff5516b2f76b454bf7c15'
		speak.say("which city's forecast would you like ?")
		with sr.Microphone() as source:
			speak.say('Hey I am Listening ')
			speak.runAndWait()
			audio2 = recogniser.listen(source)
		try:
			put_weather=recogniser.recognize_google(audio2)
			put1_weather=put1_weather.lower()
			put1_weather = put1_weather.strip()
			location = put1_weather

			url = "http://api.openweathermap.org/data/2.5/find?q=%s&units=metric&APPID=%s" %(location,APIKEY)
			response = requests.get(url)
			response_dict = json.loads(response.text)
		
			weather_today = response_dict['list'][0]
			speak.say ("Today's date is",date.today())
			frame.displayText("The average temperature today is", str(weather_today['main']['temp'])+"˚C."\
			, "You should expect", str(london_uk_today['weather'][0]['description'])+".")
		except:
			speak.say('Unable to retrieve data!')


		

class GUI(tk.Frame):
	def __init__(self, arg):
		tk.Frame.__init__(self,*args,**kwargs)

		#insert GUI objects
		#frame and all have to be designed

		speak.say('''Hi mortal ! Loquacious Spider here .''')
		speak.say( ''' Would like news or weather information or facts ?''')

	def OnClicked(self):
		recogniser = sr.Recognizer()
		with sr.Microphone() as source:
			speak.say('Hey I am Listening ')
			speak.runAndWait()
			audio = recogniser.listen(source)
		try:
			put=recogniser.recognize_google(audio)

			self.displayText(put)
			self.textBox.insert('1.2',put)
			put=put.lower()
			put = put.strip()
			link=put.split()
			voice(self,put,link)
		except sr.UnknownValueError:
			speak.say("Could not understand audio")
		except sr.RequestError as e:
			speak.say("Could not request results")
		
