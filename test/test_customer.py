#!usr/bin/env python3

import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    # def setUp(self) -> None:
        # cust = Customer("Test Person", 12345)
    
    def test_fields(self):
        cust = Customer("Test Person", 12345)
        self.assertEqual(cust.name, "Test Person")
        self.assertEqual(cust.id, 1)
        self.assertEqual(cust.zipcode, 12345)
        self.assertEqual(len(cust.accts), 0)
        cust2 = Customer("Test Person 2", 34567)
        self.assertEqual(cust2.id, 2)
        
