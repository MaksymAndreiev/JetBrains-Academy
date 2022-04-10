import random
import sqlite3
import os.path

accounts = []


def generate_number() -> str:
    num_list = [str(random.randint(0, 9)) for i in range(10)]
    IIN = '400000'
    return IIN + ''.join(num_list)


def check_number(number: str) -> list:
    orig_num = list(number)
    drop_last = orig_num[:-1]
    mult = [int(drop_last[i]) if i % 2 != 0 else 2 * int(drop_last[i]) for i in range(len(drop_last))]
    nine = [i if i <= 9 else i - 9 for i in mult]
    if (sum(nine) + int(orig_num[-1])) % 10 == 0:
        return orig_num
    else:
        return None


def valid_card(number: str) -> bool:
    if check_number(number) is None:
        return False
    else:
        return True


def set_number() -> int:
    number = check_number(generate_number())
    while number == None:
        number = check_number(generate_number())
    return int(''.join(number))


def set_PIN() -> str:
    PIN = str(random.randint(0, 9999)).zfill(4)
    return PIN


class Account:
    number = None
    PIN = None
    balance = None

    def __init__(self, number, PIN, balance):
        self.number = number
        self.PIN = PIN
        self.balance = balance

    def check_number(self, number: int):
        return number == self.number

    def check_PIN(self, PIN_code: str):
        return PIN_code == self.PIN

    def add_income(self, income: int):
        self.balance += income
        cur.execute(f'UPDATE card SET balance = {self.balance} WHERE number = {self.number}')
        conn.commit()
        print('Income was added!')


def log_in(account: Account):
    if account.check_number(int(number)) and account.check_PIN(PIN):
        return 1
    else:
        return 0


def logged_in(account: Account):
    while True:
        choice = input('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n')
        if int(choice) == 1:
            print('Balance: ' + str(account.balance))
        elif int(choice) == 2:
            income = input('Enter income:')
            account.add_income(int(income))
        elif int(choice) == 3:
            print('Transfer')
            card = input('Enter card number:\n')
            if not valid_card(card):
                print('Probably you made a mistake in the card number. Please try again!')
                continue
            if int(card) == account.number:
                print("You can't transfer money to the same account!")
                continue
            tmp_acc = cur.execute(f'SELECT * FROM card WHERE number={card}').fetchone()
            if tmp_acc is not None:
                money = int(input('Enter how much money you want to transfer:\n'))
                if money > account.balance:
                    print('Not enough money!')
                else:
                    cur.execute(f'UPDATE card SET balance = balance - {money} WHERE number = {account.number}')
                    cur.execute(f'UPDATE card SET balance = balance + {money} WHERE number = {card}')
                    conn.commit()
                    print('Success!')
            else:
                print('Such a card does not exist.')
                continue
        elif int(choice) == 4:
            cur.execute(f'DELETE FROM card WHERE number ={account.number}')
            conn.commit()
            print('The account has been closed!')
        elif int(choice) == 5:
            print('You have successfully logged out!')
            break
        elif int(choice) == 0:
            print("Bye!")
            exit(1)


if __name__ == '__main__':
    db = 'E:/MineProjects/Simple Banking System/Simple Banking System/task/card.s3db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    if os.stat(db).st_size == 0:
        cur.execute('''CREATE TABLE card (
        id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
        )''')
    while True:
        inpt = input('1. Create an account\n2. Log into account\n0. Exit\n')
        if int(inpt) == 1:
            acc = Account(set_number(), set_PIN(), 0)
            print('Your card has been created')
            print('Your card number:')
            print(acc.number)
            print('Your card PIN:')
            print(acc.PIN)
            cur.execute(
                'INSERT INTO card(number, pin, balance) VALUES (' + str(acc.number) + ',' + str(
                    acc.PIN) + ', ' + str(acc.balance) + ')')
            conn.commit()
        elif int(inpt) == 2:
            number = input('Enter your card number:\n')
            PIN = input('Enter your PIN:\n')
            tmp_acc = cur.execute(f'SELECT * FROM card WHERE number={number}').fetchone()
            if tmp_acc is not None:
                if not number == tmp_acc[1] or not PIN == tmp_acc[2]:
                    print('Wrong card number or PIN!')
                else:
                    acc_ex = cur.execute(f'SELECT * FROM card WHERE number={number}').fetchone()
                    acc = Account(int(acc_ex[1]), int(acc_ex[2]), acc_ex[3])
                    print('You have successfully logged in!')
                    logged_in(acc)
            else:
                print('Wrong card number or PIN!')
        elif int(inpt) == 0:
            print("Bye!")
            break
