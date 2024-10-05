import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    uniq = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(uniq) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [pd.NA]})
    return pd.DataFrame({'SecondHighestSalary': [uniq.iloc[1]]})