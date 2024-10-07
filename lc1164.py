import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    p = products[products['change_date'] <= '2019-08-16']
    g = p.groupby('product_id')['change_date'].max().reset_index()
    t = p.merge(g, on=['product_id', 'change_date'], how='inner')
    s = products[['product_id', 'change_date']].merge(t, on=['product_id', 'change_date'], how='left')
    r = s.groupby('product_id')['new_price'].max().reset_index().fillna(10)
    r.columns = ['product_id', 'price']
    return r


data = {
    'product_id': [1, 2, 1, 1, 2, 3],
    'new_price': [20, 50, 30, 35, 65, 20],
    'change_date': ['2019-08-14', '2019-08-14', '2019-08-15', '2019-08-16', '2019-08-17', '2019-08-18']
}

df = pd.DataFrame(data)

# Convert 'change_date' to datetime
df['change_date'] = pd.to_datetime(df['change_date'])

print(price_at_given_date(df))