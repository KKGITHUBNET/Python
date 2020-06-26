import sqlite3

db = sqlite3.connect("contacts.db")

for row in db.execute("SELECT * FROM contacts"):
    print(row)