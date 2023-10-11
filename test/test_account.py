#!/usr/bin/env python3

import unittest
import unittest.mock
from io import StringIO
from contextlib import contextmanager
from account import Account
from customer import Customer

@contextmanager
def mock_input(cmd):
    with unittest.mock.patch("sys.stdin", StringIO(cmd)):
        yield cmd

class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self._cust = Customer("Test Person", 12345)
        self._acct = Account(self._cust.name,
                             self._cust.id,
                             "Regular",
                             1111)
        
    def test_acct_attributes(self):
        self.assertEqual(self._acct.owner_name, self._cust.name)
        self.assertEqual(self._acct.owner_id, self._cust.id)
        self.assertEqual(self._acct.acct_type, "Regular")
        self.assertEqual(self._acct.balance, 0.00)
        self.assertEqual(self._acct.acct_number, 1111)
        self.assertEqual(len(self._acct.holdings), 0)
        self.assertEqual(len(self._acct.transactions), 0)

    def test_acct_deposit(self):
        with mock_input("100"):
            self._acct.deposit()
        self.assertEqual(self._acct.balance, 100)
        
        with mock_input("abcd\n1"):
            self._acct.deposit()
        self.assertEqual(self._acct.balance, 101)

    def test_acct_withdraw(self):
        with mock_input("100\n50"):
            self._acct.deposit()
            self._acct.withdraw()
        self.assertEqual(self._acct.balance, 50)

    def tearDown(self) -> None:
        Customer.unique_id = 1