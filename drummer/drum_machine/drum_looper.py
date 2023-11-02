from scamp import *
from customtkinter import *
from time import sleep
from pyautogui import *
from darkdetect import isDark
from os import name
from os.path import dirname, abspath
from sys import argv
from drum_styles import *


class DrumMachine:
	def __init__(self):
		super().__init__()

		# variables
		self.TEMPO = 100
		self.NEW_TEMPO = self.TEMPO

		self.SESSION = Session(tempo=self.TEMPO)

		if name == "posix":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "/asssets/BrushOrpheus.sf2"
		elif name == "nt":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "\\assets\\BrushOrpheus.sf2"
		
		self.DRUMMER = self.SESSION.new_part("Brush", soundfont=self.BRUSH_SOUNDFONT)

		self.BEATS = [1, 2, 3, 4]
		self.CURRENT_BEAT = 0

		self.RIDE = False
		self.SNARE = False

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
	
	def update_style(self):
		if self.CURRENT_STYLE < len(self.STYLES) - 1:
			self.CURRENT_STYLE += 1
		else:
			self.CURRENT_STYLE = 0
	
	def update_alternate(self):
		if self.CURRENT_ALTERNATE < 6:
			self.CURRENT_ALTERNATE += 1
		else:
			self.CURRENT_ALTERNATE = 0
	
	def update_tempo(self, value):
		if self.TEMPO != self.NEW_TEMPO:
			self.TEMPO = self.NEW_TEMPO
			self.SESSION.set_tempo_target(self.TEMPO, 4 - self.CURRENT_BEAT)
	
	def start_loop(self):
		fork(play_bg, args=(self.DRUMMER,))
		sleep(1)
		while self.CURRENT_BEAT < len(self.BEATS):
			drum_pattern(self.RIDE, self.SNARE, self.STYLES[self.CURRENT_STYLE], self.CURRENT_ALTERNATE, self.BEATS[self.CURRENT_BEAT], self.DRUMMER)
			self.CURRENT_BEAT += 1
			if self.CURRENT_BEAT == len(self.BEATS):
				self.CURRENT_BEAT = 0
	
	def kill_loop(self):
		self.SESSION.kill()
	
	def start_listener(self):
		self.SESSION.register_keyboard_listener(on_press=self.keyboard_input, on_release=self.keyboard_output)


class DrumGUI(CTk):
	def __init__(self, drum_machine):
		super().__init__()
		# fonts
		self.font_bold_large = CTkFont(family="Noto Sans Black", size=50)
		self.font_bold_small = CTkFont(family="Noto Sans Black", size=25)

		self.font_regular_large = CTkFont(family="Noto Sans Regular", size=50)
		self.font_regular_small = CTkFont(family="Noto Sans Regular", size=25)

		self.font_emoji_large = CTkFont(family="Noto Color Emoji", size=50)
		self.font_emoji_small = CTkFont(family="Noto Color Emoji", size=25)

		# main window layout
		self.title("jazz drummer")
		self.geometry("500x500")
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

		# frames
		self.frame_title = CTkFrame(self)
		self.frame_title.grid(row=0, column=0, padx=20, pady=(0, 5), sticky="new")
		self.frame_title.grid_columnconfigure(0, weight=1)

		self.frame_tempo = CTkFrame(self)
		self.frame_tempo.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
		self.frame_tempo.grid_columnconfigure(0, weight=1)

		# self.frame_style = CTkFrame(self)
		# self.frame_style.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
		# self.frame_style.grid_columnconfigure((1, 0), weight=1)
		# self.frame_style.grid_columnconfigure((2, 0), weight=0)
		# self.frame_style.grid_columnconfigure((2, 1), weight=1)
		# self.frame_style.grid_columnconfigure((2, 2), weight=0)

		# self.frame_instrument = CTkFrame(self)
		# self.frame_instrument.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
		# self.frame_instrument.grid_columnconfigure(0, weight=1)
		# self.frame_instrument.grid_columnconfigure(1, weight=1)

		# title
		self.title_label = CTkLabel(self.frame_title, text="jazz drummer", font=self.font_bold_large)
		self.title_label.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

		# tempo
		self.CURRENT_TEMPO = drum_machine.TEMPO
		self.tempo_label = CTkLabel(self.frame_tempo, text=str(self.CURRENT_TEMPO) + " bpm", font=self.font_bold_small)
		self.tempo_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
		self.tempo_slider = CTkSlider(self.frame_tempo, from_=60, to=200, command=self.on_click)
		self.tempo_slider.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
		self.tempo_slider.set(self.CURRENT_TEMPO)
		self.tempo_slider.bind("<ButtonRelease-1>", lambda update_tempo: self.update_tempo(0, drum_machine))

		# style


		# instruments

	def on_click(self, value):
		self.CURRENT_TEMPO = int(self.tempo_slider.get())
		self.tempo_label.configure(text=str(self.CURRENT_TEMPO) + " bpm")
	
	def update_tempo(self, value, drum_machine):
		if drum_machine.TEMPO != self.CURRENT_TEMPO:
			drum_machine.TEMPO = self.CURRENT_TEMPO
			drum_machine.SESSION.set_tempo_target(drum_machine.TEMPO, 4 - drum_machine.CURRENT_BEAT)

def start_drum_machine():
	looper = DrumMachine()

	def run_gui():
		app = DrumGUI(looper)
		app.protocol("WM_DELETE_WINDOW", looper.kill_loop)
		app.mainloop()

	fork_unsynchronized(run_gui)
	looper.start_loop()


start_drum_machine()