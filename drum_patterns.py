from scamp import Session
from drum_map import *

tempo = 100

session = Session(tempo=tempo)

drum = session.new_part("Brush", soundfont=brush)


def playnote(drum_note, length):
	if len(drum_note) == 1:
		drum.play_note(drum_note[0], 1, length)
	elif len(drum_note) > 1:
		drum.play_chord(drum_note, 1, length)


def play_bg():
	while True:
		drum.play_note(electric_snare, 1, 4)


def drum_pattern(ride, snare, genre, alternate, note):
	if genre == "samba":
		samba_pattern(ride, snare, alternate, note)
	elif genre == "mambo":
		mambo_pattern(ride, snare, note)
	elif genre == "bossa_nova":
		bossa_nova_pattern(ride, snare, alternate, note)
	elif genre == "ballroom":
		ballroom_pattern(ride, snare, note)
	elif genre == "jazz":
		jazz_pattern(ride, snare, alternate, note)
	elif genre == "waltz":
		waltz_pattern(ride, snare, alternate, note)


def samba_pattern(ride, snare, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if alternate == 0 or alternate > 1:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], sixteenth_note)
			playnote([snare_drum], sixteenth_note)
			playnote([pedal_hi_hat, cymbal], sixteenth_note)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], sixteenth_note)
			playnote([snare_drum], sixteenth_note)
			playnote([pedal_hi_hat, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note)
			playnote([bass_drum_1, cymbal], sixteenth_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note)
			playnote([bass_drum_1], sixteenth_note)
		elif note == 2:
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note)
			playnote([snare_drum, cymbal], sixteenth_note)
			playnote([pedal_hi_hat], sixteenth_note)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note)
		elif note == 3:
			playnote([bass_drum_1], sixteenth_note)
			playnote([snare_drum, cymbal], sixteenth_note)
			playnote([pedal_hi_hat], sixteenth_note)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note)
			playnote([bass_drum_1], sixteenth_note)


def mambo_pattern(ride, snare, note):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], quarter_note)
	elif note == 2:
		playnote([pedal_hi_hat, snare_drum, cymbal], eighth_note)
		playnote([bass_drum_1], eighth_note)
	elif note == 3:
		playnote([cymbal], eighth_note)
		playnote([cymbal], eighth_note)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom], eighth_note)
		playnote([low_mid_tom, cymbal], eighth_note)


def bossa_nova_pattern(ride, snare, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat
	
	if alternate == 0 or alternate > 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([bass_drum_1, cymbal], eighth_note)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)
			playnote([snare_drum, cymbal], eighth_note)
			playnote([cymbal], eighth_note)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note)

def ballroom_pattern(ride, snare, note):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], eighth_note)
		playnote([cymbal], triplet_eighth_note)
		playnote([cymbal], triplet_eighth_note)
		playnote([snare_drum], triplet_eighth_note)
	elif note == 2:
		playnote([pedal_hi_hat, cymbal], eighth_note)
		playnote([snare_drum, cymbal], eighth_note)
	elif note == 3:
		playnote([bass_drum_1, cymbal], eighth_note)
		playnote([cymbal], eighth_note)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom, cymbal], eighth_note)
		playnote([low_mid_tom, cymbal], eighth_note)


def jazz_pattern(ride, snare, alternate, note):
	if ride:
		cymbal = ride_cymbal_2
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat
	
	if alternate == 0 or alternate > 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([bass_drum_1, snare_drum], triplet_quarter_note * 2)
			playnote([bass_drum_1, cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([cymbal], quarter_note)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([cymbal, snare_drum], quarter_note)
		elif note == 3:
			playnote([cymbal], quarter_note)
		elif note == 4:
			playnote([cymbal, snare_drum], quarter_note)


def waltz_pattern(ride, snare, alternate, note):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if alternate == 0 or alternate > 6:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], quarter_note)
		elif note == 3:
			playnote([snare_drum, cymbal], quarter_note)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([snare_drum], quarter_note)
		elif note == 3:
			playnote([snare_drum], quarter_note)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([snare_drum, cymbal], triplet_quarter_note)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], quarter_note)
		elif note == 3:
			playnote([cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2)
			playnote([snare_drum], triplet_quarter_note)
		elif note == 2:
			playnote([cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([snare_drum, cymbal], quarter_note)
	elif alternate == 6:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([cymbal], triplet_quarter_note)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2)
			playnote([bass_drum_1, cymbal], triplet_quarter_note)