import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns',None)
pd.set_option('display.width', None)
pd.options.display.float_format = '{:.2f}'.format

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

data_types = employees.dtypes

numeric_columns = employees.columns[(data_types == 'float64') | (data_types == 'int64')]

numeric_employees = employees[numeric_columns]

numeric_employees = numeric_employees.drop('separated_ny', axis = 1)

employee_correlations = numeric_employees.corr()

employee_correlations

mask = np.triu(np.ones_like(employee_correlations, dtype=bool))

f, ax = plt.subplots(figsize=(6, 4))

ax.set_xticklabels(ax.get_xticklabels(), rotation = 30)

ax.set_yticklabels(ax.get_yticklabels(), rotation = 90)

sns.heatmap(employee_correlations, mask=mask, cmap="YlGnBu", center=0)
            
plt.show()            

plt.savefig('chapter_03_video_03_end_viz.svg', transparent=True, bbox_inches = "tight")
           
