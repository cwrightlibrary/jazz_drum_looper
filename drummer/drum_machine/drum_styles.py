from midi_mapping import *
from note_durations import *

def playnote(drum_note, length, drummer):
	if len(drum_note) == 1:
		drummer.play_note(drum_note[0], 1, length)
	elif len(drum_note) > 1:
		drummer.play_chord(drum_note, 1, length)


def play_bg(drummer):
	while True:
		drummer.play_note(electric_snare, 1, 4)


def drum_pattern(ride, snare, genre, alternate, note, drummer):
	if genre == "samba":
		samba_pattern(ride, snare, alternate, note, drummer)
	elif genre == "mambo":
		mambo_pattern(ride, snare, note, drummer)
	elif genre == "bossa_nova":
		bossa_nova_pattern(ride, snare, alternate, note, drummer)
	elif genre == "ballroom":
		ballroom_pattern(ride, snare, note, drummer)
	elif genre == "jazz":
		jazz_pattern(ride, snare, alternate, note, drummer)
	elif genre == "waltz":
		waltz_pattern(ride, snare, alternate, note, drummer)


def samba_pattern(ride, snare, alternate, note, drummer):
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
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1, cymbal], sixteenth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], sixteenth_note, drummer)
			playnote([snare_drum], sixteenth_note, drummer)
			playnote([pedal_hi_hat, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, cymbal], sixteenth_note, drummer)
			playnote([snare_drum], sixteenth_note, drummer)
			playnote([pedal_hi_hat, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1, cymbal], sixteenth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1, cymbal], sixteenth_note, drummer)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1], sixteenth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note, drummer)
			playnote([snare_drum, cymbal], sixteenth_note, drummer)
			playnote([pedal_hi_hat], sixteenth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1], sixteenth_note, drummer)
			playnote([snare_drum, cymbal], sixteenth_note, drummer)
			playnote([pedal_hi_hat], sixteenth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], sixteenth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([pedal_hi_hat, snare_drum, cymbal], sixteenth_note, drummer)
			playnote([bass_drum_1], sixteenth_note, drummer)


def mambo_pattern(ride, snare, note, drummer):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], quarter_note, drummer)
	elif note == 2:
		playnote([pedal_hi_hat, snare_drum, cymbal], eighth_note, drummer)
		playnote([bass_drum_1], eighth_note, drummer)
	elif note == 3:
		playnote([cymbal], eighth_note, drummer)
		playnote([cymbal], eighth_note, drummer)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom], eighth_note, drummer)
		playnote([low_mid_tom, cymbal], eighth_note, drummer)


def bossa_nova_pattern(ride, snare, alternate, note, drummer):
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
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([bass_drum_1, cymbal], eighth_note, drummer)
		elif note == 4:
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)
			playnote([snare_drum, cymbal], eighth_note, drummer)
			playnote([cymbal], eighth_note, drummer)
			playnote([bass_drum_1, snare_drum, cymbal], eighth_note, drummer)

def ballroom_pattern(ride, snare, note, drummer):
	if ride:
		cymbal = ride_cymbal_1
	else:
		cymbal = closed_hi_hat
	
	if snare:
		snare_drum = side_stick
	else:
		snare_drum = pedal_hi_hat

	if note == 1:
		playnote([bass_drum_1, cymbal], eighth_note, drummer)
		playnote([cymbal], triplet_eighth_note, drummer)
		playnote([cymbal], triplet_eighth_note, drummer)
		playnote([snare_drum], triplet_eighth_note, drummer)
	elif note == 2:
		playnote([pedal_hi_hat, cymbal], eighth_note, drummer)
		playnote([snare_drum, cymbal], eighth_note, drummer)
	elif note == 3:
		playnote([bass_drum_1, cymbal], eighth_note, drummer)
		playnote([cymbal], eighth_note, drummer)
	elif note == 4:
		playnote([bass_drum_1, pedal_hi_hat, low_mid_tom, cymbal], eighth_note, drummer)
		playnote([low_mid_tom, cymbal], eighth_note, drummer)


def jazz_pattern(ride, snare, alternate, note, drummer):
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
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([bass_drum_1, snare_drum], triplet_quarter_note * 2, drummer)
			playnote([bass_drum_1, cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note, drummer)
		elif note == 2:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([cymbal], quarter_note, drummer)
		elif note == 4:
			playnote([cymbal, snare_drum], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note, drummer)
		elif note == 2:
			playnote([cymbal, snare_drum], quarter_note, drummer)
		elif note == 3:
			playnote([cymbal], quarter_note, drummer)
		elif note == 4:
			playnote([cymbal, snare_drum], quarter_note, drummer)


def waltz_pattern(ride, snare, alternate, note, drummer):
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
			playnote([bass_drum_1, cymbal], quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum, cymbal], quarter_note, drummer)
	elif alternate == 1:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum], quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum], quarter_note, drummer)
	elif alternate == 2:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
	elif alternate == 3:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([snare_drum, cymbal], triplet_quarter_note, drummer)
	elif alternate == 4:
		if note == 1:
			playnote([bass_drum_1, cymbal], quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], quarter_note, drummer)
		elif note == 3:
			playnote([cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
	elif alternate == 5:
		if note == 1:
			playnote([bass_drum_1, cymbal], triplet_quarter_note * 2, drummer)
			playnote([snare_drum], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum, cymbal], quarter_note, drummer)
	elif alternate == 6:
		if note == 1:
			playnote([bass_drum_1, snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 2:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([cymbal], triplet_quarter_note, drummer)
		elif note == 3:
			playnote([snare_drum, cymbal], triplet_quarter_note * 2, drummer)
			playnote([bass_drum_1, cymbal], triplet_quarter_note, drummer)