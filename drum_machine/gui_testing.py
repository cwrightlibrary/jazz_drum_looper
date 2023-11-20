from customtkinter import *
from tkinter import PhotoImage
from os.path import dirname, join, realpath
from darkdetect import isDark

def import_image(arg):
	if isDark():
		df = "drumset_dark"
	else:
		df = "drumset_light"
	loc = join(dirname(realpath(__file__)), "assets", df, arg)
	img = PhotoImage(file=loc)

	return img

class App(CTk):
	def __init__(self):
		super().__init__()
		# main configuration
		self.title("drummer")
		self.geometry("800x600")
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=0)
		self.grid_columnconfigure(1, weight=0)

		# fonts
		self.font_h1 = CTkFont(size=30, weight="bold")
		self.font_h2 = CTkFont(size=21, weight="bold")
		self.font_p = CTkFont(size=16)

		# frames
		self.sidebar_frame = CTkFrame(self, corner_radius=0)
		self.sidebar_frame.grid(row=0, column=0, padx=(0, 20), pady=0, sticky="nsew")
		self.sidebar_frame.grid_rowconfigure(0, weight=0)
		self.sidebar_frame.grid_columnconfigure(0, weight=1)

		self.tabview_frame = CTkFrame(self)
		self.tabview_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
		self.tabview_frame.grid_rowconfigure(0, weight=1)
		self.tabview_frame.grid_columnconfigure(0, weight=1)

		# sidebar
		self.sidebar_title = CTkLabel(self.sidebar_frame, text="drummer", font=self.font_h1)
		self.sidebar_title.grid(row=0, column=0, padx=40, pady=20)

		# tabview
		self.tabview = CTkTabview(self.tabview_frame)
		self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
		self.tabview.add("jazz")
		self.tabview.add("bossa nova")
		self.tabview.set("jazz")

		# jazz
		self.jazz_ride_icons = [import_image("ridef.png"), import_image("ridet.png"), import_image("ridefh.png"), import_image("rideth.png")]
		self.jazz_low_tom_icons = [import_image("low_tomf.png"), import_image("low_tomt.png"), import_image("low_tomfh.png"), import_image("low_tomth.png")]
		self.jazz_bass_icons = [import_image("bassf.png"), import_image("basst.png"), import_image("bassfh.png"), import_image("bassth.png")]

		self.jazz_ride = CTkButton(self.tabview.tab("jazz"), text="", image=self.jazz_ride_icons[0], fg_color="transparent", bg_color="transparent")
		self.jazz_ride.grid(row=0, column=0, padx=(10, 250), pady=10, sticky="s")

		self.jazz_low_tom = CTkButton(self.tabview.tab("jazz"), text="", image=self.jazz_low_tom_icons[0], fg_color="transparent", bg_color="transparent")
		self.jazz_low_tom.grid(row=0, column=0, padx=0, pady=10, sticky="s")

		self.jazz_bass = CTkButton(self.tabview.tab("jazz"), text="", image=self.jazz_bass_icons[0], fg_color="transparent", bg_color="transparent")
		self.jazz_bass.grid(row=0, column=1, padx=10, pady=10, sticky="s")



app = App()
app.mainloop()