#Project 8. this is the first one with github! gotta make sure to frequently submit changes
#This is a simple GUI that asks for the user's information before putting it in a Database.
from tkinter import *
from tkinter import ttk
root = Tk()
class GreetingApp:
    def __init__ (self, master):
        frame1 = ttk.Frame(master, height = 200, width=300)
        frame1.pack()
        #Entry for the name
        self.name = ttk.Entry(frame1)
        self.name.grid()
        #birthday Entry
        self.bday = ttk.Entry(frame1)
        self.bday.grid()
        #email Entry
        self.email = ttk.Entry(frame1)
        self.email.grid()
        #phone number Entry
        self.phone = ttk.Entry(frame1)
        self.phone.grid()
        #address Entry
        self.address = ttk.Entry(frame1)
        self.address.grid()
        #dropdown for contact method
        self.contact = ttk.Combobox(frame1, state= "readonly",values = ["Email", "Phone", "Text"])
        self.contact.grid()
        #button to submit the information
        self.btn1 = ttk.Button(frame1, text="Submit")
        self.btn1.config(command=self.method1)
        self.btn1.grid()
    def method1(self):
        #should be that the sampleDB is given a new set of values
        print("Hello WORLD")
app = GreetingApp(root)
root.mainloop()
