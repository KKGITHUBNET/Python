import sqlite3

db = sqlite3.connect("contacts.db")

new_email = 'ud@update.com'
phone = input("please enter phone number: ")
phone = int(phone)

# update_sql = "UPDATE contacts set email = '{}' WHERE name = 'KK' and phone = '{}'".format(new_email,phone)
#update_sql = "DELETE FROM contacts  WHERE name = 'Keval'"
# db.execute(update_sql)

update_sql = "UPDATE contacts set email = ? WHERE phone = ?"
#print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql,(new_email,phone))
#update_cursor.execute(update_sql,(new_email,)) # You need to pass argument as a tuple.

print("{} rows were updated.".format(update_cursor.rowcount))

update_cursor.connection.commit()   # This commits the cursor statements
update_cursor.close()





db.close()
