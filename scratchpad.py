from customtkinter import *
from threading import Thread
from time import sleep


class App(CTk):
	def __init__(self):
		super().__init__()
		self.geometry("400x250")
		self.button = CTkButton(self, text="Test")
		self.button.pack(padx=20, pady=20)


def test_loop():
	while True:
		print("test")
		sleep(1)

thread = Thread(target=test_loop)
thread.daemon = True
thread.start()
app = App()
app.mainloop()
