import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    r = request_accepted.groupby('accepter_id')['requester_id'].count().reset_index()
    p = request_accepted.groupby('requester_id')['accepter_id'].count().reset_index()
    r.columns = ['id', 'num']
    p.columns = ['id', 'num']
    r = r.merge(p, left_on='id', right_on='id', how='outer')
    r = r.fillna(0)
    r['num'] = r.apply(lambda x: int(x['num_x'] + x['num_y']), axis=1)
    g = r.sort_values('num', ascending=False).head(1)
    return g[['id', 'num']]

data = {
    'requester_id': [1, 1, 2, 3],
    'accepter_id': [2, 3, 3, 4],
    'accept_date': ['2016/06/03', '2016/06/08', '2016/06/08', '2016/06/09']
}

# Create the DataFrame
df = pd.DataFrame(data)
print(most_friends(df))