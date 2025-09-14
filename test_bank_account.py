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

    def test_withdraw_with_overdraft_limit(self):
        account = BankAccount()
        account.deposit(30)
        account.set_overdraft_limit(50)
        account.withdraw(70)  # 30 + 50 overdraft = 80 available
        self.assertEqual(account.balance, -40)

    def test_withdraw_exceeds_overdraft_limit(self):
        account = BankAccount()
        account.deposit(20)
        account.set_overdraft_limit(50)
        with self.assertRaises(ValueError):
            account.withdraw(80)  # 20 + 50 overdraft = 70 available, 80 exceeds
    
if __name__ == '__main__':
    unittest.main()