from tkinter import *

class Application():
    def __init__(self):
        self.main = main
        self.main_canvas()
        main.mainloop()

    def main_canvas(self):

        self.main.title("Muts'sen")
        self.main.geometry("800x600")
        self.main.resizable(False, False)
        self.main.configure(background = "#f8faca")

main = Tk()

Application()