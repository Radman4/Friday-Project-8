#Project 8. this is the first one with github! gotta make sure to frequently submit changes
#This is a simple GUI that asks for the user's information before putting it in a Database.
from tkinter import *
from tkinter import ttk
root = Tk()
class GreetingApp:
    def __init__ (self, master):
        #label for the name
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #birthday label
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #email label
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #phone number label
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #address label
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #dropdown for contact method
        self.label1 = ttk.Label(master, text = "Hello!")
        self.label1.grid()
        #button to submit the information
        self.btn1 = ttk.Button(master, text="Submit")
        self.btn1.config(command=self.method1)
        self.btn1.grid()
    def method1(self):
        #should be that the sampleDB is given a new set of values
        print("Hello WORLD")
app = GreetingApp(root)
root.mainloop()
