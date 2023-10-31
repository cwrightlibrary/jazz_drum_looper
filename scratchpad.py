from customtkinter import *


class TempoSlider(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.h1_font = CTkFont(family="Aptos", size=30, weight="bold")
		self.h2_font = CTkFont(family="Aptos", size=24, weight="bold")
		self.h3_font = CTkFont(family="Aptos", size=20)

		self.current_tempo = 100
		
		self.tempo_label = CTkLabel(self, text=str(self.current_tempo) + " bpm", font=self.h1_font)
		self.tempo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
		
		self.tempo_slider = CTkSlider(self, from_=60, to=200, command=self.click_tempo_slider)
		self.tempo_slider.set(self.current_tempo)
		self.tempo_slider.bind("<ButtonRelease-1>", self.release_tempo_slider)
		self.tempo_slider.grid(row=1, column=0, padx=20, pady=10)
	
	def click_tempo_slider(self):
		pass

	def release_tempo_slider(self):
		pass


class App(CTk):
	def __init__(self):
		super().__init__()
		self.geometry("500x500")
		self.columnconfigure((0, 0), weight=1)
		self.rowconfigure((0, 0), weight=1)
		
		self.tempo_frame = CTkFrame(self)
		self.tempo_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nse")

		self.tempo_slider = TempoSlider(self.tempo_frame)


app = App()
app.mainloop()