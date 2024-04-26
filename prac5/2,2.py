import sqlite3
import unittest

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        if balance < amount:
            return "Недостаточно средств на счете"
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        return f"Баланс счета {self.account_number}: {balance}"

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account_number = 1234567890
        self.bank_account = BankAccount(self.account_number)
        self.bank_account.create_account(1000)

    def tearDown(self):
        self.bank_account.close_account()

    def test_deposit(self):
        self.assertEqual(self.bank_account.deposit(500), "500 средств успешно зачислены на счет 1234567890")
        self.assertEqual(self.bank_account.check_balance(), "Баланс счета 1234567890: 1500.0")

    def test_withdraw_with_enough_balance(self):
        self.assertEqual(self.bank_account.withdraw(500), "500 средств успешно сняты с счета 1234567890")
        self.assertEqual(self.bank_account.check_balance(), "Баланс счета 1234567890: 500.0")

    def test_withdraw_with_insufficient_balance(self):
        self.assertEqual(self.bank_account.withdraw(1500), "Недостаточно средств на счете")
        self.assertEqual(self.bank_account.check_balance(), "Баланс счета 1234567890: 1000.0")

if __name__ == '__main__':
    unittest.main()
