import pandas as pd
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort scores in descending order
    scores = scores.sort_values('score', ascending=False).reset_index(drop=True)
    
    # Rank the scores using the 'dense' method to handle ties
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    return scores[['score', 'rank']]