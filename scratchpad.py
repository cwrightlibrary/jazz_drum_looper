from scamp import *
from customtkinter import *
from time import sleep
from pyautogui import *
from darkdetect import isDark
from os import name
from os.path import dirname, abspath
from sys import argv

# --- TESTING AREA --- #



# --- TESTING AREA --- #

class DrumMachine:
	def __init__(self):
		super().__init__()

		# variables
		self.TEMPO = 100
		self.NEW_TEMPO = self.TEMPO

		self.SESSION = Session(tempo=self.TEMPO)

		if name == "posix":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "/BrushOrpheus.sf2"
		elif name == "nt":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "\\BrushOrpheus.sf2"
		
		self.DRUMMER = self.SESSION.new_part("Brush", soundfont=self.BRUSH_SOUNDFONT)

		self.BEATS = [1, 2, 3, 4]
		self.CURRENT_BEAT = 0

		self.RIDE = True
		self.SNARE = True

		self.STYLES = ["samba", "mambo", "bossa_nova", "ballroom", "jazz", "waltz"]
		self.ALTERNATES = [
			["one-hand", "two-hand"],
			["no alternates"],
			["2-3  clave", "2-3", "1 bar clave", "1 bar clave (alt)", "3-2 clave", "3-2"],
			["no alternates"],
			["swing", "swing (more bass)", "swing (less cymbal)", "quarter-notes"],
			["tennessee", "musette", "swing", "swing (more bass)", "swing (less cymbal)", "swing (offset pedal)", "swing (offset pedal alt)"]
		]

		self.CURRENT_STYLE = 4
		self.CURRENT_ALTERNATE = 0

		# color styles
		self.TOGGLE_ON = "#3b8ed0"
		self.TOGGLE_OFF = "#939ba2"
	
	def auto_theme(self):
		if isDark():
			self.TOGGLE_ON = "#1f6aa5"
			self.TOGGLE_OFF = "#4a4d50"
		else:
			self.TOGGLE_ON = "#3b8ed0"
			self.TOGGLE_OFF = "#939ba2"
	
	def keyboard_input(self, name, number):
		if name == "right":
			if self.CURRENT_STYLE < len(self.STYLES) - 1:
				self.CURRENT_STYLE += 1
			else:
				self.CURRENT_STYLE = 0
		elif name == "left":
			if self.CURRENT_ALTERNATE < 6:
				self.CURRENT_ALTERNATE += 1
			else:
				self.CURRENT_ALTERNATE = 0
	
	def keyboard_output(self, name, number):
		if name == "up":
			if self.TEMPO != self.NEW_TEMPO:
				self.TEMPO = self.NEW_TEMPO


# --- TESTING AREA --- #



# --- TESTING AREA --- #