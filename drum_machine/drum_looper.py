from scamp import *
from customtkinter import *
from time import sleep
from pyautogui import *
from darkdetect import isDark
from os import name
from os.path import dirname, abspath
from sys import argv
from drum_styles import *
from midi_mapping import *


class DrumMachine:
	def __init__(self):
		super().__init__()

		# variables
		self.TEMPO = 100
		self.NEW_TEMPO = self.TEMPO

		self.SESSION = Session(tempo=self.TEMPO).run_as_server()

		if name == "posix":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "/assets/BrushOrpheus.sf2"
		elif name == "nt":
			self.BRUSH_SOUNDFONT = dirname(abspath(argv[0])) + "\\assets\\BrushOrpheus.sf2"
		
		self.DRUMMER = self.SESSION.new_part("Brush", soundfont=self.BRUSH_SOUNDFONT)

		self.BEATS = [1, 2, 3, 4]
		self.CURRENT_BEAT = 0

		self.RIDE_BOOL = True
		self.HI_HAT_CLOSED_BOOL = False
		self.HI_HAT_OPEN_BOOL = False
		self.SNARE_BOOL = False
		self.SIDE_STICK_BOOL = False
		self.HI_HAT_PEDAL_BOOL = True

		self.INSTRUMENT_BOOLS_INDEX = [self.RIDE_BOOL, self.HI_HAT_CLOSED_BOOL, self.HI_HAT_OPEN_BOOL, self.SNARE_BOOL, self.SIDE_STICK_BOOL, self.HI_HAT_PEDAL_BOOL]

		self.RIDE = ride_cymbal_1
		self.HI_HAT_CLOSED = closed_hi_hat
		self.HI_HAT_OPEN = open_hi_hat
		self.SNARE = tap_snare
		self.SIDE_STICK = side_stick
		self.HI_HAT_PEDAL = pedal_hi_hat
		self.NO_INSTRUMENT = None

		if self.RIDE_BOOL:
			self.CYMBAL = self.RIDE
		if self.HI_HAT_CLOSED_BOOL:
			self.CYMBAL = self.HI_HAT_CLOSED
		if self.HI_HAT_OPEN_BOOL:
			self.CYMBAL = self.HI_HAT_OPEN
		if not self.RIDE_BOOL and not self.HI_HAT_CLOSED_BOOL and not self.HI_HAT_OPEN_BOOL:
			self.CYMBAL = self.NO_INSTRUMENT
		if self.SNARE_BOOL:
			self.SNARE_HIT = self.SNARE
		if self.SIDE_STICK_BOOL:
			self.SNARE_HIT = self.SIDE_STICK
		if self.HI_HAT_PEDAL_BOOL:
			self.SNARE_HIT = self.HI_HAT_PEDAL
		if not self.SNARE_BOOL and not self.SIDE_STICK_BOOL and not self.HI_HAT_PEDAL_BOOL:
			self.SNARE_HIT = self.NO_INSTRUMENT

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
		if isDark():
			self.TOGGLE_ON_TEXT = "#f5f5f5"
			self.TOGGLE_OFF_TEXT = "#595959"
		else:
			self.TOGGLE_ON_TEXT = "#0a0a0a"
			self.TOGGLE_OFF_TEXT = "#939ba2"
	
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
		print(self.ALTERNATES[self.CURRENT_STYLE][self.CURRENT_ALTERNATE])
	
	def update_tempo(self, value):
		if self.TEMPO != self.NEW_TEMPO:
			self.TEMPO = self.NEW_TEMPO
			self.SESSION.set_tempo_target(self.TEMPO, 4 - self.CURRENT_BEAT)
	
	def start_loop(self):
		fork(play_bg, args=(self.DRUMMER,))
		sleep(1)
		while self.CURRENT_BEAT < len(self.BEATS):
			if self.RIDE_BOOL:
				self.CYMBAL = self.RIDE
			elif self.HI_HAT_CLOSED_BOOL:
				self.CYMBAL = self.HI_HAT_CLOSED
			elif self.HI_HAT_OPEN_BOOL:
				self.CYMBAL = self.HI_HAT_OPEN
			if self.SNARE_BOOL:
				self.SNARE_HIT = self.SNARE
			elif self.SIDE_STICK_BOOL:
				self.SNARE_HIT = self.SIDE_STICK
			elif self.HI_HAT_PEDAL_BOOL:
				self.SNARE_HIT = self.HI_HAT_PEDAL
			
			drum_pattern(self.CYMBAL, self.SNARE_HIT, self.STYLES[self.CURRENT_STYLE], self.CURRENT_ALTERNATE, self.BEATS[self.CURRENT_BEAT], self.DRUMMER)
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
		if name == "posix":
			font_name_bold = "NotoSans-Black"
			font_name_reg = "NotoSans-Regular"
			font_name_emoji = "NotoColorEmoji-Regular"
		elif name == "nt":
			font_name_bold = "Noto Sans Black"
			font_name_reg = "Noto Sans Regular"
			font_name_emoji = "Noto ColorEmoji Regular"
		self.font_bold_large = CTkFont(family=font_name_bold, size=50)
		self.font_bold_small = CTkFont(family=font_name_bold, size=25)
		self.font_bold_extra_small = CTkFont(family=font_name_bold, size=17)

		self.font_regular_large = CTkFont(family=font_name_reg, size=50)
		self.font_regular_small = CTkFont(family=font_name_reg, size=25)
		self.font_regular_extra_small = CTkFont(family=font_name_reg, size=17)

		self.font_emoji_large = CTkFont(family=font_name_emoji, size=50)
		self.font_emoji_small = CTkFont(family=font_name_emoji, size=25)
		self.font_emoji_extra_small = CTkFont(family=font_name_emoji, size=17)

		# main window layout
		self.title("jazz drummer")
		self.geometry("800x600")
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

		# frames
		self.frame_title = CTkFrame(self)
		self.frame_title.grid(row=0, column=0, columnspan=2, padx=20, pady=(0, 5), sticky="new")
		self.frame_title.grid_columnconfigure(0, weight=1)

		self.frame_tempo = CTkFrame(self)
		self.frame_tempo.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
		self.frame_tempo.grid_columnconfigure(0, weight=1)

		self.frame_style = CTkFrame(self)
		self.frame_style.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
		self.frame_style.grid_columnconfigure(0, weight=1)
		self.frame_style.grid_columnconfigure(1, weight=1)
		self.frame_style.grid_columnconfigure(2, weight=1)
		self.frame_style.grid_rowconfigure(0, weight=1)
		self.frame_style.grid_rowconfigure(1, weight=1)

		self.frame_alternates = CTkFrame(self, width=600)
		self.frame_alternates.grid(row=2, column=1, rowspan=2, padx=(10, 20), pady=10, sticky="nsew")
		self.frame_alternates.grid_columnconfigure(0, weight=1)
		self.frame_alternates.grid_rowconfigure(0, weight=1)
		self.frame_alternates.grid_rowconfigure(1, weight=1)
		self.frame_alternates.grid_rowconfigure(2, weight=1)
		self.frame_alternates.grid_rowconfigure(3, weight=1)
		self.frame_alternates.grid_rowconfigure(4, weight=1)
		self.frame_alternates.grid_rowconfigure(5, weight=1)
		self.frame_alternates.grid_rowconfigure(6, weight=1)
		self.frame_alternates.grid_rowconfigure(7, weight=1)

		self.frame_instruments = CTkFrame(self)
		self.frame_instruments.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
		self.frame_instruments.grid_columnconfigure(0, weight=1)
		self.frame_instruments.grid_columnconfigure(1, weight=1)
		self.frame_instruments.grid_columnconfigure(1, weight=1)
		self.frame_instruments.grid_rowconfigure(0, weight=1)
		self.frame_instruments.grid_rowconfigure(1, weight=1)

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

		#style
		self.style_button_index = []
		for style in range(len(drum_machine.STYLES)):
			self.style_button = CTkButton(self.frame_style, text=drum_machine.STYLES[style], font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda style_num=style: self.select_style(drum_machine, style_num))
			self.style_button_index.append(self.style_button)
			
			if style < 3:
				self.style_button.grid(row=0, column=style, padx=5, pady=5, sticky="nsew")
			else:
				self.style_button.grid(row=1, column=style - 3, padx=5, pady=5, sticky="nsew")
			
			if style == drum_machine.CURRENT_STYLE:
				self.style_button_index[style].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
		
		self.alternate_width_label = CTkLabel(self.frame_alternates, text="alternate styles", font=self.font_bold_small)
		self.alternate_width_label.grid(row=0, column=0, padx=20, pady=10, sticky="new")
		self.alternate_button_index = []
		self.add_alternates(drum_machine)

		# instruments
		self.ride_button = CTkButton(self.frame_instruments, text="ride", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_ON_TEXT, command=lambda : self.select_instrument(drum_machine, 0))
		self.ride_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

		self.hi_hat_closed_button = CTkButton(self.frame_instruments, text="hi-hat closed", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda : self.select_instrument(drum_machine, 1))
		self.hi_hat_closed_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

		self.hi_hat_open_button = CTkButton(self.frame_instruments, text="hi-hat open", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda : self.select_instrument(drum_machine, 2))
		self.hi_hat_open_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

		self.snare_button = CTkButton(self.frame_instruments, text="snare", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda : self.select_instrument(drum_machine, 3))
		self.snare_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

		self.side_stick_button = CTkButton(self.frame_instruments, text="side stick", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda : self.select_instrument(drum_machine, 4))
		self.side_stick_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

		self.hi_hat_pedal_button = CTkButton(self.frame_instruments, text="hi-hat pedal", font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_ON_TEXT, command=lambda : self.select_instrument(drum_machine, 5))
		self.hi_hat_pedal_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

		self.instrument_buttons_index = [self.ride_button, self.hi_hat_closed_button, self.hi_hat_open_button, self.snare_button, self.side_stick_button, self.hi_hat_pedal_button]

	def on_click(self, value):
		self.CURRENT_TEMPO = int(self.tempo_slider.get())
		self.tempo_label.configure(text=str(self.CURRENT_TEMPO) + " bpm")
	
	def update_tempo(self, value, drum_machine):
		if drum_machine.TEMPO != self.CURRENT_TEMPO:
			drum_machine.TEMPO = self.CURRENT_TEMPO
			drum_machine.SESSION.set_tempo_target(drum_machine.TEMPO, 4 - drum_machine.CURRENT_BEAT)

	def select_style(self, drum_machine, style_num):
		drum_machine.CURRENT_STYLE = style_num
		for s in range(len(self.style_button_index)):
			if s == style_num:
				self.style_button_index[s].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			else:
				self.style_button_index[s].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
		self.add_alternates(drum_machine)
	
	def add_alternates(self, drum_machine):
		if len(self.alternate_button_index) > 0:
			for alt in self.alternate_button_index:
				alt.destroy()
		self.alternate_button_index = []
		for alt in range(len(drum_machine.ALTERNATES[drum_machine.CURRENT_STYLE])):
			self.alt_style = CTkButton(self.frame_alternates, text=drum_machine.ALTERNATES[drum_machine.CURRENT_STYLE][alt], font=self.font_bold_extra_small, fg_color="transparent", text_color=drum_machine.TOGGLE_OFF_TEXT, command=lambda alt_num=alt:self.select_alternate(drum_machine, alt_num))
			self.alt_style.grid(row=alt + 1, column=0, padx=5, pady=2, sticky="nsew")
			self.alternate_button_index.append(self.alt_style)
			
			if alt == drum_machine.CURRENT_ALTERNATE:
				self.alternate_button_index[alt].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			if len(drum_machine.ALTERNATES[drum_machine.CURRENT_STYLE]) == 1:
				self.alternate_button_index[0].configure(state="disabled")
	
	def select_alternate(self, drum_machine, alt_num):
		drum_machine.CURRENT_ALTERNATE = alt_num
		for a in range(len(self.alternate_button_index)):
			if a == alt_num:
				self.alternate_button_index[a].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			else:
				self.alternate_button_index[a].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
	
	def select_instrument(self, drum_machine, instrument_index):
		if instrument_index == 0:
			if drum_machine.RIDE_BOOL:
				self.instrument_buttons_index[0].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[0].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			self.instrument_buttons_index[1].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			self.instrument_buttons_index[2].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
		elif instrument_index == 1:
			self.instrument_buttons_index[0].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			if drum_machine.HI_HAT_CLOSED_BOOL:
				self.instrument_buttons_index[1].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[1].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			self.instrument_buttons_index[2].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
		elif instrument_index == 2:
			self.instrument_buttons_index[0].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			self.instrument_buttons_index[1].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			if drum_machine.HI_HAT_OPEN_BOOL:
				self.instrument_buttons_index[2].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[2].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
		if instrument_index == 3:
			if drum_machine.SNARE_BOOL:
				self.instrument_buttons_index[3].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[3].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			self.instrument_buttons_index[4].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			self.instrument_buttons_index[5].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
		elif instrument_index == 4:
			self.instrument_buttons_index[3].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			if drum_machine.SIDE_STICK_BOOL:
				self.instrument_buttons_index[4].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[4].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
			self.instrument_buttons_index[5].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
		elif instrument_index == 5:
			self.instrument_buttons_index[3].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			self.instrument_buttons_index[4].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			if drum_machine.HI_HAT_PEDAL_BOOL:
				self.instrument_buttons_index[5].configure(text_color=drum_machine.TOGGLE_OFF_TEXT)
			else:
				self.instrument_buttons_index[5].configure(text_color=drum_machine.TOGGLE_ON_TEXT)
		
		if instrument_index == 0:
			if drum_machine.RIDE_BOOL:
				drum_machine.RIDE_BOOL = False
				drum_machine.CYMBAL = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.RIDE_BOOL = True
				drum_machine.CYMBAL = drum_machine.RIDE
			drum_machine.HI_HAT_CLOSED_BOOL = False
			drum_machine.HI_HAT_OPEN_BOOL = False
		elif instrument_index == 1:
			drum_machine.RIDE_BOOL = False
			if drum_machine.HI_HAT_CLOSED_BOOL:
				drum_machine.HI_HAT_CLOSED_BOOL = False
				drum_machine.CYMBAL = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.HI_HAT_CLOSED_BOOL = True
				drum_machine.CYMBAL = drum_machine.HI_HAT_OPEN
			drum_machine.HI_HAT_OPEN_BOOL = False
		elif instrument_index == 2:
			drum_machine.RIDE_BOOL = False
			drum_machine.HI_HAT_CLOSED_BOOL = False
			if drum_machine.HI_HAT_OPEN_BOOL:
				drum_machine.HI_HAT_OPEN_BOOL = False
				drum_machine.CYMBAL = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.HI_HAT_OPEN_BOOL = True
				drum_machine.CYMBAL = drum_machine.HI_HAT_CLOSED
		if instrument_index == 3:
			if drum_machine.SNARE_BOOL:
				drum_machine.SNARE_BOOL = False
				drum_machine.SNARE_HIT = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.SNARE_BOOL = True
				drum_machine.SNARE_HIT = drum_machine.SNARE
			drum_machine.SIDE_STICK_BOOL = False
			drum_machine.HI_HAT_PEDAL_BOOL = False
		elif instrument_index == 4:
			drum_machine.SNARE_BOOL = False
			if drum_machine.SIDE_STICK_BOOL:
				drum_machine.SIDE_STICK_BOOL = False
				drum_machine.SNARE_HIT = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.SIDE_STICK_BOOL = True
				drum_machine.SNARE_HIT = drum_machine.SIDE_STICK
			drum_machine.HI_HAT_PEDAL_BOOL = False
		if instrument_index == 5:
			drum_machine.SNARE_BOOL = False
			drum_machine.SIDE_STICK_BOOL = False
			if drum_machine.HI_HAT_PEDAL_BOOL:
				drum_machine.HI_HAT_PEDAL_BOOL = False
				drum_machine.SNARE_HIT = drum_machine.NO_INSTRUMENT
			else:
				drum_machine.HI_HAT_PEDAL_BOOL = True
				drum_machine.SNARE_HIT = drum_machine.HI_HAT_PEDAL


def start_drum_machine():
	looper = DrumMachine()

	def run_gui():
		app = DrumGUI(looper)
		app.protocol("WM_DELETE_WINDOW", looper.kill_loop)
		app.mainloop()

	looper.SESSION.fork(looper.start_loop)
	run_gui()


start_drum_machine()
