from scamp import *
from drum_map import *

session = Session(tempo=100)

drum = session.new_part("Brush", soundfont=brush)
drum2 = session.new_part("Brush", soundfont=brush)

def play_bg():
	while True:
		drum.play_note(electric_snare, 1, 4)

fork(play_bg)

while True:
	drum2.play_note(ride_bell, .5, 1)

# play_bg()
