import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    t = customers.merge(orders['customerId'], left_on='id', right_on='customerId', how='left')
    p = t[(t['customerId'].isna())]
    return pd.DataFrame({'Customers':p['name']})


customers_data = {
    'id': [5, 2, 4, 1, 3],
    'name': ['wyu{sk', 'rgt', 'hbrmrz', 'tmjow', 'ynrl{wq']
}

# Create Customers DataFrame
customers_df = pd.DataFrame(customers_data)

# Define Orders table data
orders_data = {
    'id': [10, 3, 2, 6, 4, 8, 9, 1, 7, 5],
    'customerId': [4, 5, 3, 2, 3, 3, 3, 2, 2, 3]
}

# Create Orders DataFrame
orders_df = pd.DataFrame(orders_data)
print(find_customers(customers_df, orders_df))