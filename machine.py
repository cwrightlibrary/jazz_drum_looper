from music21 import *

fp = "C:\\Users\\CWright\\Desktop\\drum_machine\\loop.mid"
jazz_kit_drums = instrument.Instrument("jazz_kit", soundfont=fp)
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()

s = midi.translate.midiFileToStream(mf)

sp = midi.realtime.StreamPlayer(s)

jazz_kit_drums.autoAssignMidiChannel()

sp.play()