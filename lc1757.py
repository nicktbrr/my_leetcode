import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    t = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return pd.DataFrame(t['product_id'])