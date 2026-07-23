import unittest
from src.database import initialize_database
from src.product_service import list_products, inventory_summary

class DatabaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        initialize_database()

    def test_products_exist(self):
        self.assertGreater(len(list_products()), 0)

    def test_summary(self):
        self.assertGreater(inventory_summary()['total_products'], 0)

if __name__ == '__main__':
    unittest.main()
