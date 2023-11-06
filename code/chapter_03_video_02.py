import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os

pd.set_option("display.max_rows",50)
pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)
pd.options.display.float_format = "{:.2f}".format

os.getcwd()

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

data_types = employees.dtypes

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_employees = employees[numeric_columns]

numeric_employees = numeric_employees.drop('separated_ny', axis = 1)

employee_correlations = numeric_employees.corr()
employee_correlations_sorted = employee_correlations.unstack().sort_values() 

print(employee_correlations)

plt.matshow(employee_correlations)
plt.show()