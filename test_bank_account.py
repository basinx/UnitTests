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

    def test_transfer_success(self):
        account1 = BankAccount(100)
        account2 = BankAccount(50)
        account1.transfer(70, account2)
        self.assertEqual(account1.balance, 30)
        self.assertEqual(account2.balance, 120)

    def test_transfer_insufficient_funds(self):
        account1 = BankAccount(40)
        account2 = BankAccount(10)
        with self.assertRaises(ValueError):
            account1.transfer(50, account2)

    def test_transfer_with_overdraft_limit(self):
        account1 = BankAccount(20)
        account2 = BankAccount(0)
        account1.set_overdraft_limit(30)
        account1.transfer(40, account2)  # 20 + 30 overdraft = 50 available
        self.assertEqual(account1.balance, -20)
        self.assertEqual(account2.balance, 40)

    def test_transfer_exceeds_overdraft_limit(self):
        account1 = BankAccount(10)
        account2 = BankAccount(0)
        account1.set_overdraft_limit(20)
        with self.assertRaises(ValueError):
            account1.transfer(35, account2)  # 10 + 20 overdraft = 30 available, 35 exceeds

    def test_transfer_negative_amount(self):
        account1 = BankAccount(100)
        account2 = BankAccount(50)
        with self.assertRaises(ValueError):
            account1.transfer(-10, account2)

    def test_transfer_zero_amount(self):
        account1 = BankAccount(100)
        account2 = BankAccount(50)
        with self.assertRaises(ValueError):
            account1.transfer(0, account2)
    
if __name__ == '__main__':
    unittest.main()