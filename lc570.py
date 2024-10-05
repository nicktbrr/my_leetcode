import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    def group(g):
        return pd.Series({'count':g['name'].size()})
    t = employee.groupby('managerId').size().reset_index(name='count')
    t = t.merge(employee, left_on='managerId', right_on='id', how='inner')
    return t[t['count'] >= 5][['name']]


data = {
    'id': [101, 102, 103, 104, 105, 106, 107],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron', 'bill'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B', 'A'],
    'managerId': [None, 101, 101, 101, 101, 101, 102]
}

employee_df = pd.DataFrame(data)
print(find_managers(employee_df))