from customtkinter import *

genres = ["samba", "mambo", "bossa_nova", "ballroom", "jazz", "waltz"]
alternates = [
	["one-hand", "two-hand"],
	["no alternates"],
	["2-3  clave", "2-3", "1 bar clave", "1 bar clave (alt)", "3-2 clave", "3-2"],
	["no alternates"],
	["swing", "swing (more bass)", "swing (less cymbal)", "quarter-notes"],
	["tennessee", "musette", "swing", "swing (more bass)", "swing (less cymbal)", "swing (offset pedal)", "swing (offset pedal alt)"]
]

genre_current = 0
alternate_current = 0

print(alternates[genre_current][alternate_current])

class Tempo(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.font = CTkFont(family="Aptos", size=25, weight="bold")
		self.current_tempo = 100

		self.tempo_label = CTkLabel(master, text="100 bpm", font=self.font)
		self.tempo_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

		self.tempo_slider = CTkSlider(master, from_=60, to=200, command=self.on_click)
		self.tempo_slider.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
		self.tempo_slider.set(100)
		self.tempo_slider.bind("<ButtonRelease-1>", self.on_release)
	
	def on_click(self, value):
		self.current_tempo = int(self.tempo_slider.get())
		self.tempo_label.configure(text=str(self.current_tempo) + " bpm")

	def on_release(self, value):
		pass


class Genre(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		global genres, genre_current
		self.font = CTkFont(family="Aptos", size=25, weight="bold")
		self.button_font = CTkFont(family="Aptos", size=30, weight="bold")
		
		self.genre_chosen_text = genres[genre_current]

		self.genre_label = CTkLabel(master, text=self.genre_chosen_text, font=self.font)
		self.genre_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

		self.genre_prev = CTkButton(master, text="◀", command=self.genre_prev_command, width=50, font=self.button_font)
		self.genre_prev.grid(row=1, column=0, padx=(5, 2), sticky="ew")

		self.genre_slider = CTkSlider(master, from_=0, to=len(genres) - 1, number_of_steps=len(genres) - 1, command=self.on_click)
		self.genre_slider.grid(row=1, column=1, padx=2, pady=5, sticky="ew")
		self.genre_slider.set(genre_current)
		self.genre_slider.bind("<ButtonRelease-1>", self.on_release)

		self.genre_next = CTkButton(master, text="▶", command=self.genre_next_command, width=50, font=self.button_font)
		self.genre_next.grid(row=1, column=2, padx=(2, 5), sticky="ew")
	
	def on_click(self, value):
		genre_current = int(self.genre_slider.get())
		self.genre_chosen_text = genres[genre_current]
		self.genre_label.configure(text=self.genre_chosen_text)

	def on_release(self, value):
		pass
		
	def genre_prev_command(self):
		pass

	def genre_next_command(self):
		pass


class Alternate(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		global genres, genre_current, alternates, alternate_current
		self.font = CTkFont(family="Aptos", size=25, weight="bold")
		self.button_font = CTkFont(family="Aptos", size=30, weight="bold")
		
		self.alternate_chosen_text = alternates[genre_current][alternate_current]

		self.alternate_label = CTkLabel(master, text=self.alternate_chosen_text, font=self.font)
		self.alternate_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

		self.alternate_prev = CTkButton(master, text="◀", command=self.alternate_prev_command, width=50, font=self.button_font)
		self.alternate_prev.grid(row=1, column=0, padx=(5, 2), sticky="ew")

		self.alternate_slider = CTkSlider(master, from_=0, to=len(alternates[[genre_current][alternate_current]]) - 1, number_of_steps=len(alternates) - 1, command=self.on_click)
		self.alternate_slider.grid(row=1, column=1, padx=2, pady=5, sticky="ew")
		self.alternate_slider.set(genre_current)
		self.alternate_slider.bind("<ButtonRelease-1>", self.on_release)

		self.alternate_next = CTkButton(master, text="▶", command=self.alternate_next_command, width=50, font=self.button_font)
		self.alternate_next.grid(row=1, column=2, padx=(2, 5), sticky="ew")
	
	def on_click(self, value):
		alternate_current = int(self.alternate_slider.get())
		self.alternate_slider.configure(to=len(alternates[genre_current][alternate_current]))
		self.alternate_chosen_text = alternates[genre_current][alternate_current]
		self.alternate_label.configure(text=self.alternate_chosen_text)

	def on_release(self, value):
		pass
		
	def alternate_prev_command(self):
		pass

	def alternate_next_command(self):
		pass


class App(CTk):
	def __init__(self):
		super().__init__()
		self.app_name_font = CTkFont(family="Aptos", size=50, weight="bold")
		self.title("jazz drummer")
		self.geometry("500x500")
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

		self.app_name_frame = CTkFrame(self)
		self.app_name_frame.grid(row=0, column=0, padx=20, pady=(0, 10), sticky="new")
		self.app_name_frame.grid_columnconfigure(0, weight=1)

		self.app_name = CTkLabel(self.app_name_frame, text="jazz drummer", font=self.app_name_font, corner_radius=6)
		self.app_name.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

		self.tempo_frame = CTkFrame(self)
		self.tempo_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
		self.tempo_frame.grid_columnconfigure(0, weight=1)

		self.tempo_slider = Tempo(self.tempo_frame)

		self.change_genre_frame = CTkFrame(self)
		self.change_genre_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
		self.change_genre_frame.grid_columnconfigure(1, weight=1)

		self.change_genre = Genre(self.change_genre_frame)

		self.alternate_pattern_frame = CTkFrame(self)
		self.alternate_pattern_frame.grid(row=4, column=0, padx=20, pady=(10, 20), sticky="nsew")
		self.alternate_pattern_frame.grid_columnconfigure(0, weight=1)

		self.alternate_pattern = Alternate(self.alternate_pattern_frame)


app = App()
app.mainloop()