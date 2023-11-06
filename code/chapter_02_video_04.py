import pandas as pd
pd.set_option('display.max_rows',50')
pd.set_option('display.max_column',20)
pd.set_option('display.width',100)

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

employees['row_id'] = range(len(employees.index))

# department_wide = employees[{'row_id', 'department'}].pivot(index = 'row_id', columns = 'department', values = 'department')
department_wide = employees.pivot(index = 'row_id', columns = 'department', values = 'department')

department_wide = department_wide.fillna(0)

# job_level_wide = employees[{'row_id', 'job_level'}].pivot(index = 'row_id', columns = 'job_level', values = 'job_level')
job_level_wide = employees.pivot(index = 'row_id', columns = 'job_level', values = 'job_level')

job_level_wide = job_level_wide.fillna(0)

def value_encoder(data, variable):
  data.loc[data[variable] != 0, variable] = 1

for data in [department_wide, job_level_wide]:
  for names in data.columns:
    value_encoder(data, names)
  
employee_complete = employees.join(
  department_wide, 
  on = 'row_id', how = 'left'
  ).join(
    job_level_wide, 
    on = 'row_id'
    )  

# employee_complete.head()