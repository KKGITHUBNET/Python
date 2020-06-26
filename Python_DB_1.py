import sqlite3

db = sqlite3.connect("contacts.db")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone Integer , email Text)")
# db.execute("INSERT INTO contacts (name,phone,email) values ('Keval','2012349773','kk.newworld@gmail.com')")
# db.execute("INSERT INTO contacts VALUES ('KK',23567,'kj@hj.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())

# for name,phone,email in cursor:
#     print(name,phone,email)
cursor.close()
#db.commit()
db.close()


