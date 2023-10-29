from scamp import Session, fork_unsynchronized
from drum_map import *
from customtkinter import CTk, CTkFont, CTkButton
from pyautogui import press
from time import sleep

tempo = 100
beat = [1, 2, 3, 4]
beat_changed = True
ride = True
beat_idx = 0
running = False

session = Session(tempo=tempo)

brush0 = session.new_part("Brush", soundfont=brush)
brush1 = session.new_part("Brush", soundfont=brush_1)
brush2 = session.new_part("Brush", soundfont=brush_2)
jazz0 = session.new_part("Jazz", soundfont=jazz)
jazz1 = session.new_part("Jazz", soundfont=jazz_1)
jazz2 = session.new_part("Jazz", soundfont=jazz_2)
jazz3 = session.new_part("Jazz", soundfont=jazz_3)
jazz4 = session.new_part("Jazz", soundfont=jazz_4)

instrument_list = [brush0, brush1, brush2, jazz0, jazz1, jazz2, jazz3, jazz4]
selected_instrument = 0

def keyboard_input(name, number):
	if name in ["up", "down"]:
		global tempo
		if name == "up":
			tempo += 25
		elif name == "down":
			tempo -= 25
		session.set_tempo_target(tempo, 1)
	elif name == "right":
		global ride
		ride = not ride
	elif name == "left":
		global selected_instrument
		global instrument_list
		if selected_instrument >= 0 and selected_instrument < len(instrument_list) - 1:
			selected_instrument += 1


def ride_swing(n):
	if n == 1:
		instrument_list[selected_instrument].play_chord([bass_drum_1, ride_cymbal_1], 1, quarter_note)
	elif n == 2:
		instrument_list[selected_instrument].play_chord([pedal_hi_hat, ride_cymbal_1], 1, triplet_quarter_note * 2)
		instrument_list[selected_instrument].play_note(ride_cymbal_1, 1, triplet_quarter_note)
	elif n == 3:
		instrument_list[selected_instrument].play_note(ride_cymbal_1, 1, quarter_note)
	elif n == 4:
		instrument_list[selected_instrument].play_note(ride_cymbal_1, 1, triplet_quarter_note * 2)
		instrument_list[selected_instrument].play_note(ride_cymbal_1, 1, triplet_quarter_note)


def hi_hat_swing(n):
	if n == 1:
		instrument_list[selected_instrument].play_chord([bass_drum_1, open_hi_hat], 1, quarter_note)
	elif n == 2:
		instrument_list[selected_instrument].play_chord([pedal_hi_hat, open_hi_hat], 1, triplet_quarter_note * 2)
		instrument_list[selected_instrument].play_note(open_hi_hat, 1, triplet_quarter_note)
	elif n == 3:
		instrument_list[selected_instrument].play_note(open_hi_hat, 1, quarter_note)
	elif n == 4:
		instrument_list[selected_instrument].play_note(open_hi_hat, 1, triplet_quarter_note * 2)
		instrument_list[selected_instrument].play_note(open_hi_hat, 1, triplet_quarter_note)


def start_loop():
	sleep(0.5)
	global beat_idx
	while beat_idx < len(beat):
		if ride:
			ride_swing(beat[beat_idx])
		else:
			hi_hat_swing(beat[beat_idx])
		beat_idx += 1
		if beat_idx == len(beat):
			beat_idx = 0


class App(CTk):
	def __init__(self):
		super().__init__()
		# self.geometry("300x300")
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