import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.guiButton = tk.Button(self.mainWin)
        self.guiButton["text"] = "Quit"
        #quickButton = guiButton["text"] = "Quit"
        self.guiButton.grid(column=0, row=0)

        self.guiButton2 = tk.Button(self.mainWin)
        self.guiButton2["text"] = "Hello"
        #quickButton2 = guiButton2["text"] = "Hello"
        self.guiButton2.grid(column=0, row=1)

        self.guiButton3 = tk.Button(self.mainWin)
        self.guiButton3["text"] = "Goodbye"
        #quickButton3 = guiButton3["text"] = "Goodbye"
        self.guiButton3.grid(column=0, row=2)

    def run(self):
        self.mainWin.mainloop()

myGui = BasicGui()
myGui.run()