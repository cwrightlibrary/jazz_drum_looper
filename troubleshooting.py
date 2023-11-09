from scamp import *
from customtkinter import *
from time import sleep
from PIL import Image, ImageTk


class DrumMachine:
	def __init__(self):
		super().__init__()
		self.SOUNDFONT = "C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\drumfont.sf2"
		self.TEMPO = 120
		self.NEW_TEMPO = 120

		self.SESSION = Session(tempo=self.TEMPO)
		self.DRUMMER = self.SESSION.new_part("Brush", soundfont=self.SOUNDFONT)

		self.BEAT = 1

		self.RIDE = 51
		self.SNARE = 27
		self.BASS = 36
		self.BRUSH = 40
	
	def loop_swirl(self):
		while True:
			self.DRUMMER.play_note(self.BRUSH, 1, 4)

	def start_loop(self):
		sleep(0.5)
		fork(self.loop_swirl)
		while self.BEAT < 5:
			whole_note = 4
			half_note = 2
			quarter_note = 1
			eighth_note = 0.5
			sixteenth_note = 0.25
			triplet_quarter_note = 0.3333333333333333
			triplet_eighth_note = 0.1666666666666667
			triplet_sixteenth_note = 0.0833333333333333
			if self.BEAT == 1:
				self.DRUMMER.play_chord([self.BASS, self.RIDE], 1, triplet_quarter_note * 2)
				self.DRUMMER.play_note(self.RIDE, 1, triplet_quarter_note)
			elif self.BEAT == 2:
				self.DRUMMER.play_chord([self.SNARE, self.RIDE], 1, triplet_quarter_note * 2)
				self.DRUMMER.play_note(self.RIDE, 1, triplet_quarter_note)
			elif self.BEAT == 3:
				self.DRUMMER.play_chord([self.BASS, self.RIDE], 1, triplet_quarter_note * 2)
				self.DRUMMER.play_note(self.RIDE, 1, triplet_quarter_note)
			elif self.BEAT == 4:
				self.DRUMMER.play_chord([self.SNARE, self.RIDE], 1, triplet_quarter_note * 2)
				self.DRUMMER.play_note(self.RIDE, 1, triplet_quarter_note)
			self.BEAT += 1
			if self.BEAT == 5:
				self.BEAT = 1
	
	def kill_loop(self):
		self.SESSION.kill()


class DrumGUI(CTk):
	def __init__(self, drum_machine):
		super().__init__()
		self.title("looper")
		self.geometry("800x600")
		self.font = CTkFont(family="Noto Sans Black", size=50)
		
		self.current_tempo = drum_machine.TEMPO
		self.tempo_label = CTkLabel(self, text=str(self.current_tempo) + " bpm", font=self.font)
		self.tempo_label.pack(padx=20, pady=(20, 10))

		self.tempo_slider = CTkSlider(self, width=600, from_= 60, to=200, command=self.on_click)
		self.tempo_slider.pack(padx=20, pady=10)
		self.tempo_slider.set(self.current_tempo)
		self.tempo_slider.bind("<ButtonRelease-1>", lambda update_tempo: self.update_tempo(0, drum_machine))

		self.snare_button_image_true = CTkImage(Image.open("C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\snare_btn_true.png"), size=(200, 294))
		self.snare_button_image_false = CTkImage(Image.open("C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\snare_btn_false.png"), size=(200, 294))
		self.snare_button_image_hover = CTkImage(Image.open("C:\\Users\\circ8\\Documents\\Chris\\jazz_drum_looper-main\\snare_btn_hover.png"), size=(200, 294))
		self.snare_bool = True

		self.snare_button = CTkButton(self, text="", image=self.snare_button_image_true, fg_color="transparent", command=self.snare_button_switch)
		self.snare_button.pack(padx=20, pady=(10, 20))
		self.snare_button.bind("<Enter>", command=self.snare_button_hover)
		self.snare_button.bind("<Leave>", command=self.snare_button_not_hover)

	def on_click(self, value):
		self.current_tempo = int(self.tempo_slider.get())
		self.tempo_label.configure(text=str(self.current_tempo) + " bpm")
	
	def update_tempo(self, value, drum_machine):
		if drum_machine.TEMPO != self.current_tempo:
			drum_machine.TEMPO = self.current_tempo
			drum_machine.SESSION.set_tempo_target(drum_machine.TEMPO, 4 - drum_machine.BEAT)
	
	def snare_button_switch(self):
		self.snare_bool = not self.snare_bool
		if self.snare_bool:
			self.snare_button.configure(image=self.snare_button_image_true)
		else:
			self.snare_button.configure(image=self.snare_button_image_false)
	
	def snare_button_hover(self):
		self.snare_button.configure(image=self.snare_button_image_hover)

	def snare_button_not_hover(self):
		if self.snare_bool:
			self.snare_button.configure(image=self.snare_button_image_true)
		else:
			self.snare_button.configure(image=self.snare_button_image_false)


def start_app():
	looper = DrumMachine()

	def run_gui():
		app = DrumGUI(looper)
		app.protocol("WM_DELETE_WINDOW", looper.kill_loop)
		app.mainloop()
	
	fork_unsynchronized(run_gui)
	looper.start_loop()


start_app()