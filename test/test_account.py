import unittest
from app import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_create_current_account(self):
        """Test creating a current account"""
        account = BankAccount("12345678", 1000, password="securepass")
        result = account.currents_account("12345678", 1000, "securepass")
        expected = {
            'type': 'Current',
            'account_number': '12345678',
            'balance': 1000,
            'password': 'securepass'
        }
        self.assertEqual(result, expected)

    def test_create_savings_account(self):
        """Test creating a savings account with interest"""
        account = BankAccount("87654321", 5000, 2.5, password="securepass")
        result = account.savings_account("87654321", 5000, 2.5, "securepass")
        expected = {
            'type': 'Saving',
            'account_number': '87654321',
            'balance': 5000,
            'interest_rate': 2.5,
            'password': 'securepass'
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
