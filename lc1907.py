import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def my_map(col):
        ls = [0]*3
        for i in col:
            if i < 20000:
                ls[0] += 1
            elif 20000 <= i <= 50000:
                ls[1] += 1
            else:
                ls[2] += 1
        d = {'category': ['Low Salary', 'Average Salary', 'High Salary'],
             'accounts_count':ls}
        return pd.DataFrame(d)
        