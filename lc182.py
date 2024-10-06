import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person[person.duplicated(subset='email',keep=False)].drop_duplicates('email')