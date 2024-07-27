import unittest
import pandas as pd
from app import load_data, compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, top_customers_by_revenue

class TestOrderAnalyzer(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        self.data = {
            'order_id': [1, 2, 3, 4],
            'customer_id': [101, 102, 101, 103],
            'order_date': ['2023-01-15', '2023-02-15', '2023-01-25', '2023-02-25'],
            'product_id': ['P1', 'P2', 'P1', 'P3'],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [100, 200, 100, 300],
            'quantity': [2, 1, 3, 1]
        }
        self.df = pd.DataFrame(self.data)
        # Create a DataFrame with missing values for testing
        self.df_with_missing = self.df.copy()
        self.df_with_missing.loc[0, 'product_price'] = None

    def test_load_data(self):
        # test successful loading
        df = load_data('orders.csv')  # Replace with your test data file
        self.assertIsInstance(df, pd.DataFrame)
        print("\nUnit Test Passed: load_data()")
        # test error handling (optional)
        # test for FileNotFoundError, EmptyDataError, etc.

    def test_compute_revenue_by_month(self):
        revenue_by_month = compute_revenue_by_month(self.df)
        self.assertIsInstance(revenue_by_month, pd.Series)
        # adding more specific assertions based on expected results
        print("\nUnit Test Passed: compute_revenue_by_month()")

    def test_compute_revenue_by_product(self):
        revenue_by_product = compute_revenue_by_product(self.df)
        self.assertIsInstance(revenue_by_product, pd.Series)
        # adding more specific assertions based on expected results
        print("\nUnit Test Passed: compute_revenue_by_product()")

    def test_compute_revenue_by_customer(self):
        revenue_by_customer = compute_revenue_by_customer(self.df)
        self.assertIsInstance(revenue_by_customer, pd.Series)
        # adding more specific assertions based on expected results
        print("\nUnit Test Passed: compute_revenue_by_customer()")

    def test_top_customers_by_revenue(self):
        revenue_by_customer = compute_revenue_by_customer(self.df)
        top_customers = top_customers_by_revenue(revenue_by_customer, 2)
        self.assertIsInstance(top_customers, pd.Series)
        self.assertEqual(len(top_customers), 2)
        # adding more specific assertions based on expected results
        print("\nUnit Test Passed: top_customers_by_revenue()")

if __name__ == '__main__':
    unittest.main()
