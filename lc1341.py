import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    t = movie_rating.merge(users, on='user_id').sort_values('name')
    t1 = t.groupby('name')['rating'].count().reset_index()
    n = t1[t1['rating'] == t1['rating'].max()].iloc[0]
    name = pd.DataFrame({'results':[n[0]]})
    movie_rating = movie_rating.merge(movies, on='movie_id')
    d = movie_rating[(movie_rating['created_at'] >= '2020-02-01') & movie_rating['created_at'] <= '2020-02-30']
    g = d.groupby('title')['rating'].mean().reset_index()
    g = g[g['rating'] == g['rating'].max()]
    print(g)
    return name
    