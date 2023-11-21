from customtkinter import *
from PIL import Image
from os.path import dirname, join, realpath
from darkdetect import isDark

def import_image(arg):
	dd = "drumset_dark"
	dl = "drumset_light"

	dark_loc = join(dirname(realpath(__file__)), "assets", dd)
	light_loc = join(dirname(realpath(__file__)), "assets", dl)

	img_for_size = Image.open(join(dark_loc, arg))
	size = [img_for_size.width, img_for_size.height]

	img = CTkImage(dark_image=Image.open(join(dark_loc, arg)), light_image=Image.open(join(light_loc, arg)), size=size)

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
		self.font_h2 = CTkFont(size=21)
		self.font_p = CTkFont(size=16)
		self.font_p_bold = CTkFont(size=16, weight="bold")

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
		self.tabview.tab("jazz").grid_columnconfigure(0, weight=1)
		self.jazz_frame_instruments = CTkFrame(self.tabview.tab("jazz"))
		self.jazz_frame_instruments.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
		self.jazz_frame_instruments.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
		self.jazz_frame_instruments.grid_columnconfigure(0, weight=1)

		self.jazz_label_instruments = CTkLabel(self.jazz_frame_instruments, text="instruments", font=self.font_h2)
		self.jazz_label_instruments.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

		self.jazz_bass_switch = CTkSwitch(self.jazz_frame_instruments, text="bass", font=self.font_p)
		self.jazz_bass_switch.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

		self.jazz_low_tom_switch = CTkSwitch(self.jazz_frame_instruments, text="low tom", font=self.font_p)
		self.jazz_low_tom_switch.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

		self.jazz_mid_toms_switch = CTkSwitch(self.jazz_frame_instruments, text="mid toms", font=self.font_p)
		self.jazz_mid_toms_switch.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

		self.jazz_snare_switch = CTkSwitch(self.jazz_frame_instruments, text="snare", font=self.font_p)
		self.jazz_snare_switch.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")


app = App()
app.mainloop()