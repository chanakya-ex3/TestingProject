import unittest
import pandas as pd
from  task.app import load_data, compute_revenue_by_month, compute_revenue_by_product, compute_revenue_by_customer, top_customers_by_revenue
from testing.test_cases import test_cases

class TestOrderAnalyzer(unittest.TestCase):
    def setUp(self):
        # define the list of test CSV files and corresponding test cases
        self.test_files = ['testing/test1.csv', 'testing/test2.csv', 'testing/test3.csv', 'testing/test4.csv', 'testing/test5.csv']
        self.test_cases = test_cases

    def test_load_data(self):
        # ensure that we can load data from a CSV file
        for file in self.test_files:
            df = load_data(file)
            self.assertIsInstance(df, pd.DataFrame)
            print(f"\nUnit Test Passed: load_data() for {file}")

    def test_compute_revenue_by_month(self):
        # test revenue calculation by month
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_month = compute_revenue_by_month(df)
            expected = self.test_cases[f"case{i}"]["total revenue by month"]
            self.assertEqual(revenue_by_month.sort(),expected.sort())
            print(f"\nUnit Test Passed: compute_revenue_by_month() for {file}")


    def test_compute_revenue_by_product(self):
        # test revenue calculation by product
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_product = compute_revenue_by_product(df)
            expected = self.test_cases[f"case{i}"]["total revenue by product"]
            self.assertEqual(revenue_by_product.sort(),expected.sort())
            print(f"\nUnit Test Passed: compute_revenue_by_product() for {file}")

    
    def test_compute_revenue_by_customer(self):
        # test revenue calculation by customer
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_customer = compute_revenue_by_customer(df)
            expected = self.test_cases[f"case{i}"]["total revenue by customer"]
            self.assertEqual(revenue_by_customer.sort(),expected.sort())
            print(f"\nUnit Test Passed: compute_revenue_by_customer() for {file}")

    def test_top_customers_by_revenue(self):
        # test identifying top customers by revenue
        for i, file in enumerate(self.test_files, start=1):
            df = load_data(file)
            revenue_by_customer = compute_revenue_by_customer(df)
            top_customers = top_customers_by_revenue(revenue_by_customer, 10)
            expected = self.test_cases[f"case{i}"]["top 10 customers by revenue"]
            self.assertEqual(top_customers.sort(),expected.sort())
            print(f"\nUnit Test Passed: top_customers_by_revenue() for {file}")

if __name__ == '__main__':
    unittest.main()
