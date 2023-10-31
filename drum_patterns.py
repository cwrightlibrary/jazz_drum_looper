from scamp import Session
from drum_map import *

tempo = 120

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

drum = instrument_list[selected_instrument]


def playnote(drum_note, length):
	if len(drum_note) == 1:
		drum.play_note(drum_note[0], 1, length)
	elif len(drum_note) > 1:
		drum.play_chord(drum_note, 1, length)


def drum_pattern(ride, hat, genre, alternate, note):
	if genre == "samba":
		samba_pattern(ride, hat, alternate, note)
	elif genre == "mambo":
		mambo_pattern(ride, hat, note)
	elif genre == "bossa_nova":
		bossa_nova_pattern(ride, hat, alternate, note)
	elif genre == "ballroom":
		ballroom_pattern(ride, hat, note)
	elif genre == "jazz":
		jazz_pattern(ride, hat, alternate, note)
	elif genre == "waltz":
		waltz_pattern(ride, hat, alternate, note)


def samba_pattern(ride, hat, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if alternate == 0 or alternate > 1:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([pedal_hi_hat, side_stick, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], sixteenth_note)
			playnote([side_stick], sixteenth_note)
			playnote([pedal_hi_hat, cymbal], sixteenth_note)
			playnote([bass_drum_1, side_stick, cymbal], sixteenth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], sixteenth_note)
			playnote([side_stick], sixteenth_note)
			playnote([pedal_hi_hat, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
		elif note == 4:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([pedal_hi_hat, side_stick, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([pedal_hi_hat, side_stick, cymbal], sixteenth_note)
			playnote([bass_drum_1], sixteenth_note)
		elif note == 2:
			playnote([bass_drum_1, side_stick, cymbal], sixteenth_note)
			playnote([side_stick, cymbal], sixteenth_note)
			playnote([pedal_hi_hat], sixteenth_note)
			playnote([bass_drum_1, side_stick, cymbal], sixteenth_note)
		elif note == 3:
			playnote([bass_drum_1], sixteenth_note)
			playnote([side_stick, cymbal], sixteenth_note)
			playnote([pedal_hi_hat], sixteenth_note)
			playnote([bass_drum_1, side_stick, cymbal], sixteenth_note)
		elif note == 4:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([pedal_hi_hat, side_stick, cymbal], sixteenth_note)
			playnote([bass_drum_1], sixteenth_note)


def mambo_pattern(ride, hat, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], quarter_note)
	elif note == 2:
		playnote([pedal_hi_hat, side_stick, cymbal], eighth_note)
		playnote([bass_drum_1], eighth_note)
	elif note == 3:
		playnote([cymbal], eighth_note)
		playnote([cymbal], eighth_note)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom], eighth_note)
		playnote([low_mid_tom, cymbal], eighth_note)


def bossa_nova_pattern(ride, hat, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat
	if alternate == 0 or alternate > 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)
			playnote([side_stick, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, side_stick, cymbal], eighth_note)

def ballroom_pattern(ride, hat, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], eighth_note)
		playnote([cymbal], triplet_eighth_note)
		playnote([cymbal], triplet_eighth_note)
		playnote([side_stick], triplet_eighth_note)
	elif note == 2:
		playnote([pedal_hi_hat, cymbal], eighth_note)
		playnote([side_stick, cymbal], eighth_note)
	elif note == 3:
		playnote([bass_drum_1, cymbal], eighth_note)
		playnote([cymbal], eighth_note)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom, cymbal], eighth_note)
		playnote([low_mid_tom, cymbal], eighth_note)


def jazz_pattern(ride, hat, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat
	
	if alternate == 0 or alternate > 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 4:
			playnote([cymbal, side_stick], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([bass_drum_1, side_stick], triplet_quarter_note * 2)
			playnote([bass_drum_1, cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 4:
			playnote([cymbal, side_stick], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([cymbal, side_stick], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([cymbal], quarter_note)
		elif note == 4:
			playnote([cymbal, side_stick], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([cymbal, side_stick], quarter_note)
		elif note == 3:
			playnote([cymbal], quarter_note)
		elif note == 4:
			playnote([cymbal, side_stick], quarter_note)


def waltz_pattern(ride, hat, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat
	if alternate == 0 or alternate > 6:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], quarter_note)
		elif note == 3:
			playnote([side_stick, cymbal], quarter_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([side_stick], quarter_note)
		elif note == 3:
			playnote([side_stick], quarter_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([side_stick, cymbal], triplet_quarter_note)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], quarter_note)
		elif note == 3:
			playnote([cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([side_stick], triplet_quarter_note)
		elif note == 2:
			playnote([cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([side_stick, cymbal], quarter_note)
	elif alternate == 6:
		if note == 1:
			playnote([bass_drum_1, side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([side_stick, cymbal], triplet_quarter_note * 2)
			playnote([bass_drum_1, cymbal], triplet_quarter_note)