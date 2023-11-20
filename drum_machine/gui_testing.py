from customtkinter import *

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
		self.jazz_bass = CTkButton(self.tabview.tab("jazz"), text="bass")
		self.jazz_bass.grid(row=0, column=0, padx=10, pady=10)


app = App()
app.mainloop()