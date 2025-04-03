#Project 8. this is the first one with github! gotta make sure to frequently submit changes
#This is a simple GUI that asks for the user's information before putting it in a Database.
from tkinter import *
from tkinter import ttk
root = Tk()
class GreetingApp:
    def __init__ (self, master):
        #Entry for the name
        self.entry1 = ttk.Entry(master, text = "Hello!")
        self.entry1.grid()
        #birthday Entry
        self.entry2 = ttk.Entry(master, text = "Hello!")
        self.entry2.grid()
        #email Entry
        self.entry3 = ttk.Entry(master, text = "Hello!")
        self.entry3.grid()
        #phone number Entry
        self.entry4 = ttk.Entry(master, text = "Hello!")
        self.entry4.grid()
        #address Entry
        self.entry5 = ttk.Entry(master, text = "Hello!")
        self.entry5.grid()
        #dropdown for contact method
        self.entry1 = ttk.Combobox(master, text = "Hello!")
        self.entry1.grid()
        #button to submit the information
        self.btn1 = ttk.Button(master, text="Submit")
        self.btn1.config(command=self.method1)
        self.btn1.grid()
    def method1(self):
        #should be that the sampleDB is given a new set of values
        print("Hello WORLD")
app = GreetingApp(root)
root.mainloop()
