from os import name, path
from sys import argv

# drum notes
acoustic_drum = 35
bass_drum_1 = 36
side_stick = 37
acoustic_snare = 38
hand_clap = 39
electric_snare = 40
low_floor_tom = 41
closed_hi_hat = 42
high_floor_tom = 43
pedal_hi_hat = 44
low_tom = 45
open_hi_hat = 46
low_mid_tom = 47
hi_mid_tom = 48
crash_cymbal_1 = 49
high_tom = 50
ride_cymbal_1 = 51
chinese_cymbal = 52
ride_bell = 53
tambourine = 54
splash_cymbal = 55
cowbell = 56
crash_cymbal_2 = 57
vibraslap = 58
ride_cymbal_2 = 59
hi_bongo = 60
low_bongo = 61
mute_hi_conga = 62
open_hi_conga = 63
low_conga = 64
high_timbale = 65
low_timbale = 66
high_agogo = 67
low_agogo = 68
cabasa = 69
maracas = 70
short_whistle = 71
long_whistle = 72
short_guiro = 73
long_guiro = 74
claves = 75
hi_wood_block = 76
low_wood_block = 77
mute_cuica = 78
open_cuica = 79
mute_triangle = 80
open_triangle = 81

# soundfonts/mid
if name == "posix":
	brush = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush.sf2"
	brush_1 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush1.sf2"
	brush_2 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush2.sf2"
	jazz = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz.sf2"
	jazz_1 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz1.sf2"
	jazz_2 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz2.sf2"
	jazz_3 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz3.sf2"
	jazz_4 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz4.sf2"
elif name == "nt":
	current_dir = path.dirname(path.abspath(argv[0]))
	print(current_dir)
	brush = current_dir + "\\soundfonts\\Brush.sf2"
	brush_1 = current_dir + "\\soundfonts\\Brush1.sf2"
	brush_2 = current_dir + "\\soundfonts\\Brush2.sf2"
	jazz = current_dir + "\\soundfonts\\Jazz.sf2"
	jazz_1 = current_dir + "\\soundfonts\\Jazz1.sf2"
	jazz_2 = current_dir + "\\soundfonts\\Jazz2.sf2"
	jazz_3 = current_dir + "\\soundfonts\\Jazz3.sf2"
	jazz_4 = current_dir + "\\soundfonts\\Jazz4.sf2"

# durations
whole_note = 4
half_note = 2
quarter_note = 1
eighth_note = 0.5
sixteenth_note = 0.25
triplet_quarter_note = 0.3333333333333333
triplet_eighth_note = 0.1666666666666667
triplet_sixteenth_note = 0.0833333333333333