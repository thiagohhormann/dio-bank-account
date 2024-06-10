import unittest
from datetime import datetime
from bank_account.main import create_transaction

class TestCreateTransaction(unittest.TestCase):
    def test_create_transaction_valid_deposit(self):
        transaction_type = "d"
        value = 100
        expected_history = ((transaction_type, value, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),)
        self.assertEqual(create_transaction(transaction_type, value), expected_history)

    def test_create_transaction_valid_withdrawal(self):
        transaction_type = "w"
        value = 50
        expected_history = ((transaction_type, value, datetime.now().strftime('%Y-%m-%d %H:%M:%S')),)
        self.assertEqual(create_transaction(transaction_type, value), expected_history)

    def test_create_transaction_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            create_transaction("invalid_type", 100)
        self.assertEqual(str(context.exception), "Transaction type must be [d]eposit or [w]ithdrawal")




if __name__ == '__main__':
    unittest.main()
