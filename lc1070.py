import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    first_sales = sales.groupby('product_id')['year'].min().reset_index()

    # Merge with product table to get product names
    m = first_sales.merge(sales, on=['product_id', 'year'], how='inner')
    
    # # Select and rename the necessary columns
    m = m[['product_id', 'year', 'quantity', 'price']]
    m.columns = ['product_id', 'first_year', 'quantity', 'price']
    return m

sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}
sales_df = pd.DataFrame(sales_data)

# Create the Product DataFrame
product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}
product_df = pd.DataFrame(product_data)

print(sales_analysis(sales_df, product_df))