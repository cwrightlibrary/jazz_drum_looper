from scamp import Session, fork_unsynchronized
from drum_map import *
from customtkinter import CTk, CTkFont, CTkButton
from pyautogui import press
from time import sleep
from drum_patterns import *

beat = [1, 2, 3, 4]
beat_changed = True
ride = True
hat = False
beat_idx = 0
running = False

def keyboard_input(name, number):
	if name in ["up", "down"]:
		global tempo
		if name == "up":
			tempo += 25
		elif name == "down":
			tempo -= 25
		session.set_tempo_target(tempo, 1)
	elif name == "right":
		global ride, hat
		ride = not ride
		hat = not hat
	elif name == "left":
		global selected_instrument
		global instrument_list
		if selected_instrument >= 0 and selected_instrument < len(instrument_list) - 1:
			selected_instrument += 1


def start_loop():
	sleep(1)
	global beat_idx
	while beat_idx < len(beat):
		drum_pattern(ride, hat, "bossa_nova", 0, beat[beat_idx])
		beat_idx += 1
		if beat_idx == len(beat):
			beat_idx = 0


class App(CTk):
	def __init__(self):
		super().__init__()
		self.geometry("300x300")
		self.heading_font = CTkFont(family="Aptos", size=30, weight="bold")

		self.tempo_button_up = CTkButton(self, text="🔼", command=self.press_up, font=self.heading_font)
		self.tempo_button_up.pack(padx=20, pady=(20, 10))

		self.tempo_button_down = CTkButton(self, text="🔽", command=self.press_down, font=self.heading_font)
		self.tempo_button_down.pack(padx=20, pady=10)

		self.change_kit = CTkButton(self, text="🥁", command=self.press_change_kit, font=self.heading_font)
		self.change_kit.pack(padx=20, pady=10)

		self.change_cymbal = CTkButton(self, text="📀", command=self.press_change_cymbal, font=self.heading_font)
		self.change_cymbal.pack(padx=20, pady=(10, 20))
	def press_up(self):
		press("up")
	def press_down(self):
		press("down")
	def press_change_kit(self):
		press("left")
	def press_change_cymbal(self):
		press("right")


def kill_loop():
	session.kill()


def run_gui():
	app = App()
	app.protocol("WM_DELETE_WINDOW", kill_loop)
	app.mainloop()


session.register_keyboard_listener(on_press=keyboard_input)

fork_unsynchronized(run_gui)

start_loop()
