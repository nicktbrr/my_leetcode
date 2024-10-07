import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    s = weather.shift(1)
    w = weather[(weather['temperature'] > s['temperature']) & (s['recordDate'] + pd.DateOffset(days=1) == weather['recordDate'])]
    return w[['id']]