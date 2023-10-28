from scamp import *

s = Session()

piano = s.new_part("piano").add_streaming_midi_playback(0)
synth = s.new_osc_part("vibrato", ip_address="127.0.0.1", port=57120)
silent = s.new_silent_part("silent")

s.start_transcribing()

for _ in range(4):
	piano.play_note(60, 1, 0.5)
	synth.play_note(62, 1, 0.5)
	silent.play_note(63, 1, 0.5)

s.stop_transcribing().to_score(time_signature="6/8").show()