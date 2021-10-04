from django.test import TestCase
from checkout.models import *
# Create your tests here.
class testModels(TestCase):
    def setUp(self):
        self.CheckOut = CheckOut()
        self.CheckOut.item_list = []
        self.CheckOut.tax = 0.12
        Gateway().add_item_to_database('apple', 2)
        Gateway().add_item_to_database('pear', 3)
        Gateway().add_item_to_database('banana', 1)
        Gateway().add_item_to_database('hat', 10)
        Gateway().add_item_to_database('orange', 3)
        self.CheckOut.add_item_to_list("apple", 2)
        self.CheckOut.add_item_to_list("pear", 3)
        self.CheckOut.add_item_to_list("banana", 4)
        self.CheckOut.add_item_to_list("hat", 5)
        self.CheckOut.add_item_to_list("orange", 6)
        self.CheckOut.add_item_to_list("CSC301", 7)
        
    def test_change_tax(self):
        self.CheckOut.change_tax(0.13)
        self.assertEqual(self.CheckOut.tax, 0.13)

    def test_add_item_to_list(self):
        self.assertTrue(self.CheckOut.add_item_to_list("apple", 2))
        self.assertTrue(self.CheckOut.add_item_to_list("pear", 2))
        self.assertTrue(self.CheckOut.add_item_to_list("banana", 4))
        self.assertTrue(self.CheckOut.add_item_to_list("hat", 5))
        self.assertTrue(self.CheckOut.add_item_to_list("orange", 6))
        self.assertFalse(self.CheckOut.add_item_to_list("CSC301", 7))

    def test_get_item_by_name(self):
        apple_info = self.CheckOut.get_item_by_name("apple")
        self.assertEqual(apple_info[0].get_name(), Item("apple", 2).get_name())
        dne = self.CheckOut.get_item_by_name("CSC301")
        self.assertIsNone(dne)

    def test_get_item_list(self):
        self.assertEqual(self.CheckOut.get_item_list(), self.CheckOut.item_list)

    def test_remove_item_from_list(self):
        self.CheckOut.remove_item_from_list("orange", 1)
        self.assertEqual(self.CheckOut.get_item_by_name("orange")[1], 5)
        self.CheckOut.remove_item_from_list("orange", 5)
        self.assertIsNone(self.CheckOut.get_item_by_name("orange"))
        self.CheckOut.remove_item_from_list("hat", 6)
        self.assertIsNone(self.CheckOut.get_item_by_name("hat"))

    def test_count_sum(self):
        self.assertEqual(self.CheckOut.count_sum(), 95.2)

    def test_add_discount(self):
        self.CheckOut.add_discount("apple", 0.1)
        self.assertEqual(self.CheckOut.get_item_by_name("apple")[0].discount, 0.1)
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_discount(), 0.1)
        self.CheckOut.add_discount("pear", 0.15)
        self.assertEqual(self.CheckOut.get_item_by_name("pear")[0].discount, 0.15)
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_discount(), 0.15)
        self.CheckOut.add_discount("banana", 0.2)
        self.assertEqual(self.CheckOut.get_item_by_name("banana")[0].discount, 0.2)
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_discount(), 0.2)

    def test_get_name(self):
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_name(), "apple")
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_name(), "pear")
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_name(), "banana")

    def test_get_price(self):
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_price(), 2)
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_price(), 3)
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_price(), 1)

    def test_change_name(self):
        self.CheckOut.get_item_list()[0][0].change_name("Apple")
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_name(), "Apple")
        self.CheckOut.get_item_list()[1][0].change_name("Pear")
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_name(), "Pear")
        self.CheckOut.get_item_list()[2][0].change_name("Banana")
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_name(), "Banana")

    def test_change_price(self):
        self.CheckOut.get_item_list()[0][0].change_price(2.5)
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_price(), 2.5)
        self.CheckOut.get_item_list()[1][0].change_price(3.5)
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_price(), 3.5)
        self.CheckOut.get_item_list()[2][0].change_price(1.5)
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_price(), 1.5)

    def test_change_discount(self):
        self.CheckOut.get_item_list()[0][0].change_discount(0.3)
        self.assertEqual(self.CheckOut.get_item_list()[0][0].get_discount(), 0.3)
        self.CheckOut.get_item_list()[1][0].change_discount(0.3)
        self.assertEqual(self.CheckOut.get_item_list()[1][0].get_discount(), 0.3)
        self.CheckOut.get_item_list()[2][0].change_discount(0.3)
        self.assertEqual(self.CheckOut.get_item_list()[2][0].get_discount(), 0.3)