import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates()
    highest_salary = 0
    if N >= 1 :
        highest_salary = unique_salary.nlargest(N).iloc[-1] if len(unique_salary) >= N else None
    if highest_salary is None or N < 1 :
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': [highest_salary]})