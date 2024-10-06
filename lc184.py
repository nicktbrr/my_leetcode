import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    g = employee.groupby(['departmentId'])['salary'].max().reset_index()
    t = g.merge(employee, on=['salary', 'departmentId'], how='inner')
    t = t.merge(department, left_on='departmentId', right_on='id', how='inner')
    df = pd.DataFrame({'Department':t['name_y'], 'Employee':t['name_x'], 'Salary':t['salary']})
    return df


employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}

# Create Employee DataFrame
employee_df = pd.DataFrame(employee_data)

# Define Department table data
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}

# Create Department DataFrame
department_df = pd.DataFrame(department_data)
department_highest_salary(employee_df, department_df)