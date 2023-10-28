from scamp import *
from drum_map import *

TEMPO = 150

session = Session(tempo=TEMPO)

drum = session.new_part("Brush", soundfont=brush)


def play_backbeat():
	for n in range(1, 5):
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



while True:
	play_backbeat()