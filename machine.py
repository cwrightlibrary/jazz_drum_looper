from scamp import Session, fork_unsynchronized
from drum_map import *
from customtkinter import CTk, CTkFont, CTkButton, CTkSlider
from time import sleep
from drum_patterns import *
import mido

beat = [1, 2, 3, 4]
beat_changed = True
ride = True
hat = False
beat_idx = 0
running = False
alternate_pattern = 0

patterns = ["samba", "mambo", "bossa_nova", "ballroom", "jazz", "waltz"]
pattern_idx = 4

port = mido.open_output(mido.get_output_names()[-1])
port_num = len(mido.get_output_names()) - 1
print(session.get_available_midi_input_devices())

def keyboard_input(name, number):
	if name in ["up", "down"]:
		global tempo, beat_idx
		if name == "up":
			tempo += 25
		elif name == "down":
			tempo -= 25
		remaining_beats = 4 - beat_idx
		session.set_tempo_target(tempo, remaining_beats)
		print(tempo)
	elif name == "right":
		global pattern_idx
		if pattern_idx < len(patterns) - 1:
			pattern_idx += 1
		else:
			pattern_idx = 0
		print(patterns[pattern_idx])
	elif name == "left":
		global alternate_pattern
		if alternate_pattern < 6:
			alternate_pattern += 1
		else:
			alternate_pattern = 0
		print(alternate_pattern)


def midi_input(message, dt):
	pass


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

		# self.tempo_button_up = CTkButton(self, text="🔼", command=self.press_up, font=self.heading_font)
		# self.tempo_button_up.pack(padx=20, pady=(20, 10))

		# self.tempo_button_down = CTkButton(self, text="🔽", command=self.press_down, font=self.heading_font)
		# self.tempo_button_down.pack(padx=20, pady=10)

		self.slider = CTkSlider(self, from_=60, to=290, command=self.slider_tempo)
		self.slider.pack(padx=20, pady=(20, 10))

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
	def slider_tempo(self, value):
		print(int(value))


def kill_loop():
	session.kill()


def run_gui():
	app = App()
	app.protocol("WM_DELETE_WINDOW", kill_loop)
	app.mainloop()


# session.register_keyboard_listener(on_press=keyboard_input)
# session.register_midi_listener(port_num, callback_function=midi_input)

fork_unsynchronized(run_gui)

start_loop()
