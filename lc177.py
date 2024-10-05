import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = 'getNthHighestSalary(' + str(N) + ')'
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    if N > len(employee['salary'].unique()) or N < 1:
        return pd.DataFrame({col: [pd.NA]})
    return pd.DataFrame({col: [unique_salaries[N-1]]})