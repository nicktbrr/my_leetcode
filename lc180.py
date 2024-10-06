import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:    
    logs['lag_foward1'] = logs['num'].shift(1)
    logs['lag_before1'] = logs['num'].shift(-1)
    print((logs['lag_foward1'] == logs['num'] ))

    res = logs.loc[(logs['lag_foward1'] == logs['num'] )& (logs['lag_before1'] == logs['num'])]
    print(res)
    res = res[['num']].rename(columns={'num':'ConsecutiveNums'}).drop_duplicates()

    return res 

logs_data = {
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
}

# Create the Logs DataFrame
logs_df = pd.DataFrame(logs_data)

print(consecutive_numbers(logs_df))