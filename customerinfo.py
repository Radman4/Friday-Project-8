import sqlite3
connection = sqlite3.connect('CustomerInfo.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS customer_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    contact_method TEXT NOT NULL
)''')

cursor.execute('''INSERT INTO customer_info (name, birthday, email, 
               phone, address, contact_method) VALUES (?,?,?,?,?,?);''' , 
('Johnny Test', '05/25/2007', 'blinblingsux@gmail.com', '123-456-7890', '1234 Test St, Test City, TX', 'Email'))

connection.commit()
cursor.execute("SELECT * FROM customer_info")
print(cursor.fetchall())

