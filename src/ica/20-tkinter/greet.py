import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.guiButton = tk.Button(self.mainWin)
        self.guiButton["text"] = "Quit"
        self.guiButton.grid(column=0, row=0)

        self.guiButton2 = tk.Button(self.mainWin)
        self.guiButton2["text"] = "Hello"
        self.guiButton2.grid(column=0, row=1)

        self.guiButton2["command"] = self.Hellobutton

        self.guiButton3 = tk.Button(self.mainWin)
        self.guiButton3["text"] = "Goodbye"
        self.guiButton3.grid(column=0, row=2)

        self.guiButton3["command"] = self.Goodbyebutton

        self.welcome = tk.Label(self.mainWin)
        self.welcome["text"] = "Welcome"
        self.welcome.grid(column=1, row=1)


    def run(self):
        self.mainWin.mainloop()


    def quit_callback(self):
        self.mainWin.destroy()
        self.guiButton["command"] = self.quit_callback


    def Hellobutton(self):
        self.welcome["text"] = "Hello"
        self.guiButton2.config(text="Hellos")


    def Goodbyebutton(self):
        self.guiButton3.config(text="Goodbyes")


myGui = BasicGui()
myGui.run()
myGui.quit_callback()