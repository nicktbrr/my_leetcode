import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    d = delivery.sort_values('order_date').drop_duplicates(subset=['customer_id'], keep='first')
    d['sum'] = d.apply(lambda x: 1 if x['order_date'] == x['delivery_date'] else 0, axis=1)
    return pd.DataFrame({'immediate_percentage': [d['sum'].mean()]})