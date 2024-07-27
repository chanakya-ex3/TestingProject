import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    loads the orders data from a CSV file.

    parameters:
    - file_path: str - path to the CSV file.

    returns:
    - pd.DataFrame: a DataFrame containing the order data.
    """
    try:
        df = pd.read_csv(file_path)
        # print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"error: file not found at path {file_path}")
        raise
    except pd.errors.EmptyDataError:
        print("error: no data in file.")
        raise
    except pd.errors.ParserError:
        print("error: error parsing the file.")
        raise

def compute_revenue_by_month(df: pd.DataFrame) -> list:
    """
    computes total revenue by month.

    parameters:
    - df: pd.DataFrame - DataFrame containing the order data.

    returns:
    - list: a list of tuples with months as index and total revenue as values.
    """
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_month = df.groupby('month')['total_price'].sum()
    return list(revenue_by_month.items())

def compute_revenue_by_product(df: pd.DataFrame) -> list:
    """
    computes total revenue by product.

    parameters:
    - df: pd.DataFrame - DataFrame containing the order data.

    returns:
    - list: a list of tuples with product names as index and total revenue as values.
    """
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_product = df.groupby('product_name')['total_price'].sum().sort_values(ascending=False)
    return list(revenue_by_product.items())

def compute_revenue_by_customer(df: pd.DataFrame) -> list:
    """
    computes total revenue by customer.

    parameters:
    - df: pd.DataFrame - DataFrame containing the order data.

    returns:
    - list: a list of tuples with customer IDs as index and total revenue as values.
    """
    df['total_price'] = df['product_price'] * df['quantity']
    revenue_by_customer = df.groupby('customer_id')['total_price'].sum().sort_values(ascending=False)
    return list(revenue_by_customer.items())

def top_customers_by_revenue(revenue_by_customer: list, top_n: int = 10) -> list:
    """
    identifies the top N customers by revenue.

    parameters:
    - revenue_by_customer: list - list containing total revenue by customer.
    - top_n: int - number of top customers to return.

    returns:
    - list: a list of tuples with customer IDs as index and total revenue as values for the top N customers.
    """
    return revenue_by_customer[:top_n]

def main():
    df = load_data("test1.csv")

    # compute and print the total revenue by month
    revenue_by_month = compute_revenue_by_month(df)
    print("total revenue by month:")
    print(revenue_by_month)
    # for month, revenue in revenue_by_month:
    #     print(f"{month}: {revenue}")

    # compute and print the total revenue by product
    revenue_by_product = compute_revenue_by_product(df)
    print("\ntotal revenue by product:")
    print(revenue_by_product)
    # for product, revenue in revenue_by_product:
    #     print(f"{product}: {revenue}")

    # compute and print the total revenue by customer
    revenue_by_customer = compute_revenue_by_customer(df)
    print("\ntotal revenue by customer:")
    print(revenue_by_customer)
    # for customer, revenue in revenue_by_customer:
    #     print(f"{customer}: {revenue}")

    # identify and print the top 10 customers by revenue
    top_customers = top_customers_by_revenue(revenue_by_customer)
    print("\ntop 10 customers by revenue:")
    print(top_customers)
    # for customer, revenue in top_customers:
    #     print(f"{customer}: {revenue}")

if __name__ == "__main__":
    main()
