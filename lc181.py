import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        right=employee,
        how='inner',
        left_on='managerId',
        right_on='id')
    print(df)
    emp = df[df['salary_x'] > df['salary_y']]['name_x']
    return pd.DataFrame({'Employee': emp})


employees_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

# Create the Employees DataFrame
employees_df = pd.DataFrame(employees_data)
print(find_employees(employees_df))