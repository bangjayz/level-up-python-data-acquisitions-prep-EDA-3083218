import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA

pd.set_option('display.max_rows',50)
pd.set_option('display.max_column',10)
pd.set_option('display.width',1000)
pd.options.display.float_format = '{:.20f}'.format

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

data_types = employees.dtypes

numeric_predictors = employees.columns[(data_types == 'float64') | (data_types == 'int64')]
numeric_employees = employees[numeric_predictors]
numeric_employees = numeric_employees.drop(['days_to_separate', 'separated_ny'], axis = 1)

pca = PCA(n_components = 4)
# len(numeric_employees.columns)
pca.fit(numeric_employees)

print(pca.explained_variance_ratio_)

component_number = np.arange(pca.n_components_) + 1

pca_results = pd.DataFrame()

pca_results['number'] = component_number

pca_results['eigenvalue'] = pca.explained_variance_ratio_

pca_plot = sns.relplot(x = 'number', y = 'eigenvalue', kind = 'line', data = pca_results)

plt.show()

# Xt = pd.DataFrame(pca.fit_transform(numeric_employees))
# Xt