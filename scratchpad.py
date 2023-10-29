from scamp import *
from drum_map import *
from threading import Thread

TEMPO = 100

beat = [1, 2, 3, 4]
beat_changed = True
playing = True
active_beat = 1
run = False

session = Session(tempo=TEMPO)

drum = session.new_part("Brush", soundfont=brush)

def update_tempo():
	prev_tempo = TEMPO
	while True:
		new_tempo = input("tempo: ")
		if prev_tempo != new_tempo:
			session.set_tempo_target(int(new_tempo), 1)
			prev_tempo = new_tempo


def drum_loop(n):
	if n == 1:
		drum.play_chord([bass_drum_1, ride_cymbal_1], 1, quarter_note)
	elif n == 2:
		drum.play_chord([pedal_hi_hat, ride_cymbal_1], 1, triplet_quarter_note * 2)
		drum.play_note(ride_cymbal_1, 1, triplet_quarter_note)
	elif n == 3:
		drum.play_note(ride_cymbal_1, 1, quarter_note)
	elif n == 4:
		drum.play_note(ride_cymbal_1, 1, triplet_quarter_note * 2)
		drum.play_note(ride_cymbal_1, 1, triplet_quarter_note)


def start_loop():
	for n in range(len(beat)):
		drum_loop(beat[n])


tempo_thread = Thread(target=update_tempo)
tempo_thread.start()

while True:
	start_loop()
