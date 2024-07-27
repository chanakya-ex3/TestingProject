import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    loads the orders data from a CSV file.

    parameters:
    - file_path - path to the CSV file.

    returns:
    - a dataFrame containing the order data.
    """
    try:
        df = pd.read_csv(file_path)
        # print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: No data in file.")
        raise
    except pd.errors.ParserError:
        print("Error: Error parsing the file.")
        raise

def compute_revenue_by_month(df: pd.DataFrame) -> pd.Series:
    """
    computes total revenue by month.

    parameters:
    - df  - dataFrame containing the order data.

    returns:
    - a series with months as index and total revenue as values.
    """
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_month = df.groupby('month')['total_price'].sum()
    return revenue_by_month

def compute_revenue_by_product(df: pd.DataFrame) -> pd.Series:
    """
    computes total revenue by product.

    parameters:
    - df  - a dataFrame containing the order data.

    returns:
    - a series with product names as index and total revenue as values.
    """
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_product = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False)
    return revenue_by_product

def compute_revenue_by_customer(df: pd.DataFrame) -> pd.Series:
    """
    computes total revenue by customer.

    parameters:
    - df dataFrame containing the order data.

    returns:
    - a series with customer IDs as index and total revenue as values.
    """
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_customer = df.groupby('customer_id')['total_price'].sum().sort_values(ascending=False)
    return revenue_by_customer

def top_customers_by_revenue(revenue_by_customer: pd.Series, top_n: int = 10) -> pd.Series:
    """
    identify the top N customers by revenue.

    args:
    - revenue_by_customer - Series containing total revenue by customer.
    - top_n - Number of top customers to return.

    reuturns:
    - a series with customer IDs as index and total revenue as values for the top N customers.
    """
    return revenue_by_customer.head(top_n)

def main():
    df = load_data("orders.csv")

    # compute and print the total revenue by month
    revenue_by_month = compute_revenue_by_month(df)
    print("Total Revenue by Month:")
    print(revenue_by_month)

    # compute and print the total revenue by product
    revenue_by_product = compute_revenue_by_product(df)
    print("\nTotal Revenue by Product:")
    print(revenue_by_product)

    # compute and print the total revenue by customer
    revenue_by_customer = compute_revenue_by_customer(df)
    print("\nTotal Revenue by Customer:")
    print(revenue_by_customer)

    # identify and print the top 10 customers by revenue
    top_customers = top_customers_by_revenue(revenue_by_customer)
    print("\nTop 10 Customers by Revenue:")
    print(top_customers)

if __name__ == "__main__":
    main()
