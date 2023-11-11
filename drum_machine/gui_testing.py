from customtkinter import *
from PIL import Image
from os.path import join, dirname, realpath
from darkdetect import isDark

class App(CTk):
	def __init__(self):
		super().__init__()
		self.title("gui_testing.py")
		self.geometry("500x500")

		assets_dir = join(dirname(realpath(__file__)), "assets")
		drumset_dark_dir = join(assets_dir, "drumset_dark")
		drumset_light_dir = join(assets_dir, "drumset_light")
		
		if isDark:
			dark_or_light_dir = drumset_dark_dir
		else:
			dark_or_light_dir = drumset_light_dir
		
		self.bassf_image = CTkImage(Image.open(join(dark_or_light_dir, "bassf.png")), size=(254, 254))
		self.basst_image = CTkImage(Image.open(join(dark_or_light_dir, "basst.png")), size=(254, 254))
		self.bassfh_image = CTkImage(Image.open(join(dark_or_light_dir, "bassfh.png")), size=(254, 254))
		self.bassth_image = CTkImage(Image.open(join(dark_or_light_dir, "bassth.png")), size=(254, 254))
			
		self.bass_drum_frame = CTkFrame(self, corner_radius=0)
		self.bass_drum_frame.pack()

		self.bass_drum_bool = False

		self.bass_drum_button = CTkButton(self.bass_drum_frame, text="", image=self.bassf_image, hover=False, fg_color=("gray92", "grey14"), corner_radius=0, command=self.bass_drum_switch)
		self.bass_drum_button.pack()
		self.bass_drum_button.bind("<Enter>", self.on_enter)
		self.bass_drum_button.bind("<Leave>", self.on_leave)

	def bass_drum_switch(self):
		self.bass_drum_bool = not self.bass_drum_bool
		if self.bass_drum_bool:
			self.bass_drum_button.configure(image=self.bassth_image)
		else:
			self.bass_drum_button.configure(image=self.bassfh_image)
	
	def on_enter(self, n):
		if self.bass_drum_bool:
			self.bass_drum_button.configure(image=self.bassth_image)
		else:
			self.bass_drum_button.configure(image=self.bassfh_image)
	
	def on_leave(self, n):
		if self.bass_drum_bool:
			self.bass_drum_button.configure(image=self.basst_image)
		else:
			self.bass_drum_button.configure(image=self.bassf_image)

app = App()
app.mainloop()