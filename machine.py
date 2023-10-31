from scamp import Session, fork_unsynchronized
from drum_map import *
from customtkinter import CTk, CTkFont, CTkButton, CTkSlider, CTkLabel
from time import sleep
from drum_patterns import *
from pyautogui import *
from brush_loop import *

beat = [1, 2, 3, 4]
beat_changed = True
ride = True
hat = False
beat_idx = 0
running = False
alternate_pattern = 0
new_tempo = tempo

patterns = ["samba", "mambo", "bossa_nova", "ballroom", "jazz", "waltz"]
pattern_idx = 4


def keyboard_input(name, number):
	if name == "right":
		global pattern_idx
		if pattern_idx < len(patterns) - 1:
			pattern_idx += 1
		else:
			pattern_idx = 0
	elif name == "left":
		global alternate_pattern
		if alternate_pattern < 6:
			alternate_pattern += 1
		else:
			alternate_pattern = 0
	elif name == "down":
		global instrument_list, selected_instrument
		if selected_instrument < len(instrument_list):
			selected_instrument += 1
		else:
			selected_instrument = 0
		print(selected_instrument)
		


def keyboard_output(name, number):
	if name == "up":
		global new_tempo, tempo, beat_idx
		if tempo != new_tempo:
			tempo = new_tempo
		session.set_tempo_target(tempo, 4 - beat_idx)


def start_loop():
	sleep(1)
	global beat_idx
	while beat_idx < len(beat):
		drum_pattern(ride, hat, patterns[pattern_idx], alternate_pattern, beat[beat_idx])
		beat_idx += 1
		if beat_idx == len(beat):
			beat_idx = 0


class App(CTk):
	def __init__(self):
		super().__init__()
		self.geometry("300x300")
		self.heading_font = CTkFont(family="Aptos", size=30, weight="bold")

		self.current_tempo = tempo

		self.slider = CTkSlider(self, from_=60, to=200, command=self.click_slider)
		self.slider.pack(padx=20, pady=(20, 10))
		self.slider.set(tempo)
		self.slider.bind("<ButtonRelease-1>", self.release_slider)

		self.tempo_label = CTkLabel(self, text="tempo: " + str(self.current_tempo), font=self.heading_font)
		self.tempo_label.pack(padx=20, pady=10)

		self.change_kit = CTkButton(self, text="🥁", command=self.press_change_kit, font=self.heading_font)
		self.change_kit.pack(padx=20, pady=10)

		self.change_cymbal = CTkButton(self, text="📀", command=self.press_change_cymbal, font=self.heading_font)
		self.change_cymbal.pack(padx=20, pady=20)

		self.change_drum = CTkButton(self, text="🎵", command=self.change_drum, font=self.heading_font)
		self.change_drum.pack(padx=20, pady=(10, 20))

		brush_swirl_loop.play()
	def press_change_kit(self):
		press("left")
	def press_change_cymbal(self):
		press("right")
	def click_slider(self, value):
		self.current_tempo = int(self.slider.get())
		self.tempo_label.configure(text="tempo: " + str(self.current_tempo))
		print(self.current_tempo / 100)
	def release_slider(self, value):
		global new_tempo
		new_tempo = self.current_tempo
		press("up")
	def change_drum(self):
		press("down")


def kill_loop():
	session.kill()


def run_gui():
	app = App()
	app.protocol("WM_DELETE_WINDOW", kill_loop)
	app.mainloop()


session.register_keyboard_listener(on_press=keyboard_input, on_release=keyboard_output)

fork_unsynchronized(run_gui)

start_loop()
