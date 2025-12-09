import tkinter as tk

class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()

        self.label1 = tk.Label(self.mainWin)
        self.label1["text"] = "label 1"
        self.label1["bg"] = "Blue"
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.mainWin)
        self.label2["text"] = "label 2"
        self.label2["bg"] = "Red"
        self.label2.grid(row=1, column=0)

        self.quitButton = tk.Button(self.mainWin)
        self.quitButton["text"] = "quit"
        self.quitButton["command"] = self.mainWin.destroy
        self.quitButton.grid(row=2, column=0)

        self.entry1 = tk.Entry(self.mainWin)
        self.entry1["bg"] = "Red"
        self.entry1.grid(row=3, column=0)
        self.entry1.bind("<Return>",self.entry_response)


    def entry_response(self, event):
        get_entry = self.entry1.get()
        get_entry_reverse = get_entry[::-1]
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, get_entry_reverse)




    def run(self):
        self.mainWin.mainloop()


myGui = BasicGui()
myGui.run()