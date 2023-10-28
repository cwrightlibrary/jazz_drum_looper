from scamp import *

session = Session()

brush = "C:\Users\circ8\Documents\Chris\jazz_drum_looper-main\soundfonts\Brush.sf2"


drum = session.new_part(soundfont=brush)

for pitch in [35, 51, 42, 51, 35, 51, 42, 51]:
	drum.play_note(pitch, 1, 0.5)