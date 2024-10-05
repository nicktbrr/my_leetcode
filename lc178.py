import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values('score', ascending=False)
    def rank(col):
        r = 1
        i = 0
        j = 1
        ranks = []
        ranks.append(r)
        for n in col:
            if col[i] == col[j]:
                ranks.append(r)
            else:
                r += 1
                ranks.append(r)
            i, j += 1
    