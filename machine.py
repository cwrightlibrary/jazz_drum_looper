from scamp import *
from mido import MidiFile
from os import name
from collections import namedtuple

if name == "posix":
	INPUT_MID = "/Users/christopherwright/Desktop/jazz_drum_looper-main/loop.mid"
	brush = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush.sf2"
	brush_1 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush1.sf2"
	brush_2 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Brush2.sf2"
	jazz = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz.sf2"
	jazz_1 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz1.sf2"
	jazz_2 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz2.sf2"
	jazz_3 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz3.sf2"
	jazz_4 = "/Users/christopherwright/Desktop/jazz_drum_looper-main/soundfonts/Jazz4.sf2"
elif name == "nt":
	INPUT_MID = "C\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper_main\\loop.mid"
	brush = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Brush.sf2"
	brush1 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Brush1.sf2"
	brush_2 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Brush2.sf2"
	jazz = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Jazz.sf2"
	jazz_1 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Jazz1.sf2"
	jazz_2 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Jazz2.sf2"
	jazz_3 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Jazz3.sf2"
	jazz_4 = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\soundfonts\\Jazz4.sf2"

mid = MidiFile(INPUT_MID, clip=True)
Note = namedtuple("Note", "channel pitch volume start_time length")

notes_started = {}
notes = []

for track in mid.tracks:
    t = 0
    for message in track:
        t += message.time / mid.ticks_per_beat
        if message.type == "note_off" or (message.type == "note_on" and message.velocity == 0):
            volume, start_time = notes_started[(message.note, message.channel)]
            notes.append(Note(message.channel, message.note, volume, start_time, t - start_time))
        elif message.type == "note_on":
            notes_started[(message.note, message.channel)] = message.velocity / 127, t

notes.sort(key=lambda note: note.start_time)

channels, pitches, volumes, start_times, lengths = zip(*notes)
channels = list(channels)
pitches = list(pitches)
volumes = list(volumes)
start_times = list(start_times)
lengths = list(lengths)

inter_onset_times = [t2 - t1 for t1, t2 in zip(start_times[:-1], start_times[1:])]

TEMPO = 200

session = Session(tempo=TEMPO)

drum = session.new_part("Brush", soundfont=brush)

for wait_time, pitch, length, volume in zip(inter_onset_times, pitches, lengths, volumes):
	drum.play_note(pitch, volume, length, blocking=False)
	wait(wait_time)
