import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(1,len(seat['student']), 2):
        seat['student'][i-1], seat['student'][i] = seat['student'][i], seat['student'][i-1]
    return seat
