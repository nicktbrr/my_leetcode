import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    w = world[(world['area']>= 3000000) | (world['population'] >= 25000000)]
    return w[['name', 'population', 'area']]