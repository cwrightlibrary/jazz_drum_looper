from customtkinter import *
from darkdetect import isDark

if isDark():
	toggle_off = "#4a4d50"
	toggle_on = "#1f6aa5"
else:
	toggle_off = "#939ba2"
	toggle_on = "#3b8ed0"

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
		global genres, genre_current, alternate_current
		self.font = CTkFont(family="Aptos", size=25, weight="bold")
		self.button_font = CTkFont(family="Aptos", size=25, weight="bold")
		
		self.genre_chosen_text = genres[genre_current]

		self.genre_label = CTkLabel(master, text=self.genre_chosen_text, font=self.font)
		self.genre_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

		self.genre_slider = CTkSlider(master, from_=0, to=len(genres) - 1, number_of_steps=len(genres) - 1, command=self.on_click_genre)
		self.genre_slider.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
		self.genre_slider.set(genre_current)
		self.genre_slider.bind("<ButtonRelease-1>", self.on_release_genre)

		self.alternate_prev = CTkButton(master, text="👈", command=self.alternate_prev_command, width=50, font=self.button_font)
		self.alternate_prev.grid(row=2, column=0, padx=10, sticky="e")

		self.alternate_chosen_text = alternates[genre_current][alternate_current]
		self.alternate_label = CTkLabel(master, text=self.alternate_chosen_text, font=self.font)
		self.alternate_label.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

		self.alternate_next = CTkButton(master, text="👉", command=self.alternate_next_command, width=50, font=self.button_font)
		self.alternate_next.grid(row=2, column=2, padx=10, pady=5, sticky="w")
	
	def on_click_genre(self, value):
		global alternates, alternate_current, genres, genre_current
		genre_current = int(value)
		alternate_current = 0
		self.genre_chosen_text = genres[genre_current]
		self.genre_label.configure(text=self.genre_chosen_text)
		self.alternate_chosen_text = alternates[genre_current][alternate_current]
		self.alternate_label.configure(text=self.alternate_chosen_text)
		print("genre " + str(genre_current))
		print("alternate " + str(alternate_current))

	def on_release_genre(self, value):
		pass

	def genre_prev_command(self):
		pass

	def genre_next_command(self):
		pass

	def alternate_prev_command(self):
		global alternates, alternate_current, genres, genre_current
		if alternate_current > 0:
			alternate_current -= 1
			self.alternate_chosen_text = alternates[genre_current][alternate_current]
			self.alternate_label.configure(text=self.alternate_chosen_text)
			print(alternate_current)
		else:
			alternate_current = len(alternates[genre_current]) - 1
			self.alternate_chosen_text = alternates[genre_current][alternate_current]
			self.alternate_label.configure(text=self.alternate_chosen_text)
			print(alternate_current)
	def alternate_next_command(self):
		global alternates, alternate_current, genres, genre_current
		if alternate_current < len(alternates[genre_current]) - 1:
			alternate_current += 1
			self.alternate_chosen_text = alternates[genre_current][alternate_current]
			self.alternate_label.configure(text=self.alternate_chosen_text)
			print(alternate_current)
		else:
			alternate_current = 0
			self.alternate_chosen_text = alternates[genre_current][alternate_current]
			self.alternate_label.configure(text=self.alternate_chosen_text)
			print(alternate_current)


class Instrument(CTkFrame):
	def __init__(self, master):
		super().__init__(master)
		self.font = CTkFont(family="Aptos", size=25, weight="bold")
		self.button_font = CTkFont(family="Aptos", size=50, weight="bold")

		self.instruments_label = CTkLabel(master, text="toggle instruments", font=self.font)
		self.instruments_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

		self.ride_toggle = False
		self.snare_toggle = False

		self.ride_switch = CTkSwitch(master, text="💿", font=self.button_font, switch_width=50, switch_height=25, command=self.ride_command, text_color=toggle_on)
		self.ride_switch.grid(row=1, column=0, padx=50, pady=5, sticky="ew")
		self.ride_switch.toggle()

		self.snare_switch = CTkSwitch(master, text="🥁", font=self.button_font, switch_width=50, switch_height=25, command=self.snare_command, text_color=toggle_on)
		self.snare_switch.grid(row=1, column=2, padx=50, pady=5, sticky="ew")
		self.snare_switch.toggle()
	
	def ride_command(self):
		self.ride_toggle = not self.ride_toggle
		if self.ride_toggle:
			self.ride_switch.configure(text_color=toggle_on)
		else:
			self.ride_switch.configure(text_color=toggle_off)
	
	def snare_command(self):
		self.snare_toggle = not self.snare_toggle
		if self.snare_toggle:
			self.snare_switch.configure(text_color=toggle_on)
		else:
			self.snare_switch.configure(text_color=toggle_off)
			


class App(CTk):
	def __init__(self):
		super().__init__()
		self.app_name_font = CTkFont(family="Aptos", size=50, weight="bold")
		self.title("jazz drummer")
		self.geometry("500x500")
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

		self.app_name_frame = CTkFrame(self)
		self.app_name_frame.grid(row=0, column=0, padx=20, pady=(0, 5), sticky="new")
		self.app_name_frame.grid_columnconfigure(0, weight=1)

		self.app_name = CTkLabel(self.app_name_frame, text="jazz drummer", font=self.app_name_font, corner_radius=6)
		self.app_name.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

		self.tempo_frame = CTkFrame(self)
		self.tempo_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
		self.tempo_frame.grid_columnconfigure(0, weight=1)

		self.tempo_slider = Tempo(self.tempo_frame)

		self.change_genre_frame = CTkFrame(self)
		self.change_genre_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
		self.change_genre_frame.grid_columnconfigure((1, 0), weight=1)
		self.change_genre_frame.grid_columnconfigure((2, 0), weight=0)
		self.change_genre_frame.grid_columnconfigure((2, 1), weight=1)
		self.change_genre_frame.grid_columnconfigure((2, 2), weight=0)

		self.change_genre = Genre(self.change_genre_frame)

		self.instrument_select_frame = CTkFrame(self)
		self.instrument_select_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
		self.instrument_select_frame.grid_columnconfigure(0, weight=1)
		self.instrument_select_frame.grid_columnconfigure(1, weight=1)
		self.instrument_select = Instrument(self.instrument_select_frame)


app = App()
app.mainloop()