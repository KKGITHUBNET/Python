import pytz
import sqlite3
import datetime

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    @staticmethod
    def _current_time():  # This is a static method. self should not be used in argument
        local_time = pytz.utc.localize(datetime.datetime.utcnow())
        return local_time.astimezone()


    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name,balance FROM accounts WHERE (name = ?)",(name,))
        row = cursor.fetchone()

        if row:   # is same as "if row is not NONE"
            self.name,self._balance = row
            print("Account Already exists for {}. ".format(self.name), end="")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?,?)",(name,opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end="")
        self.show_balance()


    def _save_update(self, amount):
        new_balance = self._balance + amount
        withdrawal_time = Account._current_time()
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)",(new_balance,self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)",(withdrawal_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
        finally:
            db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount/100))
        return self._balance/100

    def withdraw(self,amount : int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)",(amount,self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)",(withdrawal_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)  # This is not a static method since it is called by "self._save_method".
            print("{:.2f} withdrawn.".format(amount/100))
            return amount/100
        else:
            print("The Amount must be greater than zero and no more than account balance")
            return 0.0

    def show_balance(self):
        print("Balance on {}'s account is ${:.2f}".format(self.name, self._balance/100))


if __name__ == '__main__':
    keval = Account("KK")
    keval.deposit(10000000)
    keval.deposit(200)
    keval.deposit(300)
    keval.withdraw(500)
    keval.show_balance()

    john = Account("John")
    terry = Account("terry",100)
    mary = Account("mary",200)
    eric=Account("eric",300)

    db.close()