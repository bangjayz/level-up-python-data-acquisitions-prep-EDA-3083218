import pandas as pd

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

def z_score_maker(variable):
  variable_mean = variable.mean()
  variable_sd = variable.std()
  z_score = (variable - variable_mean) / variable_sd 
  return z_score
  
z_score_maker(employees['age'])

# data_types = employees.dtypes
# numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]
# numeric_columns = numeric_columns[numeric_columns != "separated_ny"]
# numeric_data = employees[numeric_columns]

# z_score_maker(employees['days_to_separate'])
# a = employees.groupby('separated_ny')
# a.first()
# a.get_group(0).count()
# employees[['separated_ny','department']].value_counts().pivot(index = 'separated_ny', row = 'department')
