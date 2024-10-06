import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    select_order = orders[(orders['order_date']>='2019-01-01')&(orders['order_date']<='2019-12-31')].copy()
    select_order = select_order.groupby('buyer_id')['order_id'].nunique().reset_index().rename(columns={'order_id':'orders_in_2019'})
    print(select_order)
    users = users.rename(columns={'user_id':'buyer_id'})
    df = pd.merge(users[['buyer_id','join_date']],select_order,on='buyer_id',how='left')
    print(df)
    df = df.fillna(0)
    return df
    

users_data = {
    'user_id': [1, 2, 3, 4],
    'join_date': ['2018-01-01', '2018-02-09', '2018-01-19', '2018-05-21'],
    'favorite_brand': ['Lenovo', 'Samsung', 'LG', 'HP']
}
users_data['join_date'] = pd.to_datetime(users_data['join_date'])

# Create Users DataFrame
users_df = pd.DataFrame(users_data)

# Define Orders table data
orders_data = {
    'order_id': [1, 2, 3, 4, 5, 6],
    'order_date': ['2019-08-01', '2018-08-02', '2019-08-03', '2018-08-04', '2018-08-04', '2019-08-05'],
    'item_id': [4, 2, 3, 1, 1, 2],
    'buyer_id': [1, 1, 2, 4, 3, 2],
    'seller_id': [2, 3, 3, 2, 4, 4]
}
orders_data['order_date'] = pd.to_datetime(orders_data['order_date'])
# Create Orders DataFrame
orders_df = pd.DataFrame(orders_data)

# Define Items table data
items_data = {
    'item_id': [1, 2, 3, 4],
    'item_brand': ['Samsung', 'Lenovo', 'LG', 'HP']
}

# Create Items DataFrame
items_df = pd.DataFrame(items_data)

market_analysis(users_df, orders_df, items_df)