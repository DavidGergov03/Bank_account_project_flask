import unittest
from app import Account

class TestAccount(unittest.TestCase):
    def test_deposit(self):
        acc = Account(100)
        acc.deposit(50)
        self.assertEqual(acc.balance, 150)

    def test_withdraw(self):
        acc = Account(100)
        acc.withdraw(40)
        self.assertEqual(acc.balance, 60)

if __name__ == '__main__':
    unittest.main()
