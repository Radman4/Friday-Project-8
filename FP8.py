#Project 8. this is the first one with github! gotta make sure to frequently submit changes
#This is a simple GUI that asks for the user's information before putting it in a Database.
from tkinter import *
from tkinter import ttk
import sqlite3

#allows connection to the database

root = Tk()
class GreetingApp:
    def __init__ (self, master):

        frame1 = ttk.Frame(master, height = 200, width=300)
        frame1.pack()
        #Entry for the name
        self.label1 = ttk.Label(frame1, text="Name:")
        self.label1.grid(column= 0, row= 0)
        self.name = ttk.Entry(frame1)
        self.name.grid(column= 1, row= 0)
        #birthday Entry
        self.label2 = ttk.Label(frame1, text="Birthday (MM/DD/YYYY):")
        self.label2.grid(column= 0, row = 1)
        self.bday = ttk.Entry(frame1)
        self.bday.grid(column= 1, row = 1)
        #email Entry
        self.label3 = ttk.Label(frame1, text="Email:")
        self.label3.grid(column= 0, row = 2)
        self.email = ttk.Entry(frame1)
        self.email.grid(column= 1, row = 2)
        #phone number Entry
        self.label4 = ttk.Label(frame1, text="Phone number:")
        self.label4.grid(column= 0, row = 3)
        self.phone = ttk.Entry(frame1)
        self.phone.grid(column= 1, row = 3)
        #address Entry
        self.label5 = ttk.Label(frame1, text="Address:")
        self.label5.grid(column= 0, row = 4)
        self.address = ttk.Entry(frame1)
        self.address.grid(column= 1, row = 4)
        #dropdown for contact method
        self.label6 = ttk.Label(frame1, text="Contact Method:")
        self.label6.grid(column= 0, row = 5)
        self.contact = ttk.Combobox(frame1, state= "readonly",values = ["Email", "Phone", "Text"])
        self.contact.grid(column= 1, row = 5)
        #button to submit the information
        self.btn1 = ttk.Button(frame1, text="Submit")
        self.btn1.config(command=self.method1)
        self.btn1.grid()
    def method1(self):
        #should be that the DB is given a new set of values
        name = self.name.get()
        bday = self.bday.get()
        email = self.email.get()
        phone = self.phone.get()
        address = self.address.get()
        contact = self.contact.get()
        #connect to the database
        conn = sqlite3.connect('CustomerInfo.db') 
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS customer_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_method TEXT NOT NULL
)''')
        #this is where the data is inserted into the database
        cursor.execute('''INSERT INTO customer_info 
                       (name, birthday, email, phone, address, contact_method) VALUES (?,?,?,?,?,?);''' ,
                        (name,bday,email,phone,address,contact))
        conn.commit()

app = GreetingApp(root)
root.mainloop()
