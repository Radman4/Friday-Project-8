from tkinter import *
from tkinter import ttk
root = Tk()
class GreetingApp:
    def __init__ (self, master):
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        self.btn1 = ttk.Button(master, text="Submit")
        self.btn1.config(command=self.method1)
        self.btn1.grid()
    def method1(self):
        print("Hello WORLD")
app = GreetingApp(root)
root.mainloop()
