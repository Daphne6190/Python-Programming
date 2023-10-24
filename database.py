import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

print("table created successfuly")
conn.close()
