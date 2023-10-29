from scamp import *
from drum_map import *
from customtkinter import *
from threading import Thread

tempo = 100
beat = [1, 2, 3, 4]
beat_changed = True
ride = True

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


class App(CTk):
	def __init__(self):
		super().__init__()
		self.geometry("400x250")
		self.running = False

		self.button = CTkButton(self, text="play", command=self.begin_thread)
		self.button.pack(padx=20, pady=20)
	def begin_thread(self):
		if not self.running:
			threading()
			self.running = True

app = App()


def start_loop():
	for n in beat:
		app.update()
		if ride:
			ride_swing(n)
		else:
			hi_hat_swing(n)


def threading():
	loop_thread = Thread(target=start_loop)
	loop_thread.start()


session.register_keyboard_listener(on_press=keyboard_input)

app.mainloop()

# start_loop()
