import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)

    def test_deposit(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

if __name__ == '__main__':
    unittest.main()