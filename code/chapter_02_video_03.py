# pd.set_option('display.max_rows', 50)
# pd.set_option('display.max_columns', 10)
# pd.set_option('display.width', 100)

import pandas as pd

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')
# employees.head(10)
data_types = employees.dtypes

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_columns = numeric_columns[numeric_columns != "separated_ny"]

numeric_employees = employees[numeric_columns]

numeric_employees.dtypes 
