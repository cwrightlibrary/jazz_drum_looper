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
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if alternate == 0:
		if note == 1:
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, eighth_note)
			drum.play_chord([pedal_hi_hat, side_stick, cymbal], 1, sixteenth_note)
			drum.play_chord([bass_drum_1, cymbal], 1, sixteenth_note)
		elif note == 2:
			drum.play_chord([bass_drum_1, cymbal], 1, sixteenth_note)
			drum.play_note(side_stick, 1, sixteenth_note)
			drum.play_chord([pedal_hi_hat, cymbal], 1, sixteenth_note)
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, sixteenth_note)
		elif note == 3:
			drum.play_chord([bass_drum_1, cymbal], 1, sixteenth_note)
			drum.play_note(side_stick, 1, sixteenth_note)
			drum.play_chord([pedal_hi_hat, cymbal], 1, sixteenth_note)
			drum.play_chord([bass_drum_1, cymbal], 1, sixteenth_note)
		elif note == 4:
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, eighth_note)
			drum.play_chord([pedal_hi_hat, side_stick, cymbal], 1, sixteenth_note)
			drum.play_chord([bass_drum_1, cymbal], 1, sixteenth_note)
	elif alternate == 1:
		if note == 1:
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, eighth_note)
			drum.play_chord([pedal_hi_hat, side_stick, cymbal], 1, sixteenth_note)
			drum.play_note(bass_drum_1, 1, sixteenth_note)
		elif note == 2:
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, sixteenth_note)
			drum.play_chord([side_stick, cymbal], 1, sixteenth_note)
			drum.play_note(pedal_hi_hat, 1, sixteenth_note)
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, sixteenth_note)
		elif note == 3:
			drum.play_note(bass_drum_1, 1, sixteenth_note)
			drum.play_chord([side_stick, cymbal], 1, sixteenth_note)
			drum.play_note(pedal_hi_hat, 1, sixteenth_note)
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, sixteenth_note)
		elif note == 4:
			drum.play_chord([bass_drum_1, side_stick, cymbal], 1, eighth_note)
			drum.play_chord([pedal_hi_hat, side_stick, cymbal], 1, sixteenth_note)
			drum.play_note(bass_drum_1, 1, sixteenth_note)


def mambo_pattern(ride, hat, note):
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		drum.play_chord([bass_drum_1, cymbal], 1, quarter_note)
	elif note == 2:
		drum.play_chord([pedal_hi_hat, side_stick, cymbal], 1, eighth_note)
		drum.play_note(bass_drum_1, 1, eighth_note)
	elif note == 3:
		drum.play_note(cymbal, 1, eighth_note)
		drum.play_note(cymbal, 1, eighth_note)
	elif note == 4:
		drum.play_chord([bass_drum_1, pedal_hi_hat, low_mid_tom], 1, eighth_note)
		drum.play_chord([low_mid_tom, cymbal], 1, eighth_note)


def bossa_nova_pattern(ride, hat, alternate, note):
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		pass
	elif note == 2:
		pass
	elif note == 3:
		pass
	elif note == 4:
		pass


def ballroom_pattern(ride, hat, note):
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		drum.play_chord([bass_drum_1, cymbal], 1, eighth_note)
		drum.play_note(cymbal, 1, triplet_sixteenth_note)
		drum.play_note(cymbal, 1, triplet_sixteenth_note)
		drum.play_note(side_stick, 1, triplet_sixteenth_note)
	elif note == 2:
		drum.play_chord([pedal_hi_hat, cymbal], 1, eighth_note)
		drum.play_chord([side_stick, cymbal], 1, eighth_note)
	elif note == 3:
		drum.play_chord([bass_drum_1, cymbal], 1, eighth_note)
		drum.play_note(cymbal, 1, eighth_note)
	elif note == 4:
		drum.play_chord([bass_drum_1, pedal_hi_hat, low_mid_tom, cymbal], 1, eighth_note)
		drum.play_chord([low_mid_tom, cymbal], 1, eighth_note)


def jazz_pattern(ride, hat, alternate, note):
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		pass
	elif note == 2:
		pass
	elif note == 3:
		pass
	elif note == 4:
		pass


def waltz_pattern(ride, hat, alternate, note):
	drum = instrument_list[selected_instrument]
	if ride:
		cymbal = ride_cymbal_1
	elif hat:
		cymbal = closed_hi_hat

	if note == 1:
		pass
	elif note == 2:
		pass
	elif note == 3:
		pass
	elif note == 4:
		pass