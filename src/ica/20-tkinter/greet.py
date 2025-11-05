import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        guiButton = tk.Button(self.mainWin)

    def run(self):
        self.mainWin.mainloop()

myGui = BasicGui()
myGui.run()