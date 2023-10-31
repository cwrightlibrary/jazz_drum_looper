import os
import wave
import threading
import sys
import pyaudio
from drum_patterns import tempo
import numpy


class WavePlayerLoop(threading.Thread):
	CHUNK = 1024

	def __init__(self, filepath, loop=True):
		super(WavePlayerLoop, self).__init__()
		self.filepath = os.path.abspath(filepath)
		self.loop = loop
		global tempo
		self.speed = tempo / 100
	
	def run(self):
		wf = wave.open(self.filepath, "rb")
		player = pyaudio.PyAudio()
		stream = player.open(format=player.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

		data = wf.readframes(self.CHUNK)
		while self.loop:
			stream.write(data)
			data = wf.readframes(self.CHUNK)
			if data == b"":
				wf.rewind()
				data = wf.readframes(self.CHUNK)
		
		stream.close()
		player.terminate()
	
	def play(self):
		self.start()
	
	def stop(self):
		self.loop = False


brush_swirl_loop = WavePlayerLoop("brush_loop_quiet.wav")
