import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 15)
pd.set_option('display.width',1000)
pd.options.display.float_format = '{:.2f}'.format

employees = pd.read_csv('/Users/modifero/VSCode/linkedin-python-level-up/level-up-python-data-acquisitions-prep-EDA-3083218/data/level_up_data.csv')

employees.describe(include='all')
employees.dtypes
employees.isna().sum()


# Null value handling
data_cat, data_num = [], []
for i in employees.columns:
    if employees[i].dtypes == "object":
        data_cat.append(i)
    else:
        data_num.append(i)
        
data_num = employees[[c for c in employees.columns if c in data_num]]
data_cat = employees[[c for c in employees.columns if c in data_cat]]

# # isi missing di data_num
# for i in data_num.columns:
#     data_num[i] = data_num[i].fillna(data_num[i].mean())
    
# # isi missing di data_cat
# for i in data_cat.columns:
#     data_cat[i] = data_cat[i].fillna(data_cat[i].mode()[0])

# data_cat
# data_num

# #Outliers Handling
# from collections import Counter
# import numpy as np

# all_outliers = np.array([], dtype='int64')
# outliers_counter = Counter()
# outliers_scores = None 

# for i in data_num.columns:
    
#     Q1 = np.percentile(data_num[i], 25)
#     Q3 = np.percentile(data_num[i], 75)
    
#     step = 1.5 * (Q3 - Q1)
    
#     zeros = np.zeros(len(data_num[i]))
#     above = data_num[i].values - Q3 - step
#     below = data_num[i].values - Q1 + step
#     current_outliers_scores = np.array(np.maximum(zeros, above) - 
#                                        np.minimum(zeros, below)
#                                       ).reshape([-1,1])
#     outliers_scores = current_outliers_scores if outliers_scores is None else np.hstack([outliers_scores, current_outliers_scores])
    
#     current_outliers = data_num[~((data_num[i] >= Q1 - step) & 
#                               (data_num[i] <= Q3 + step))
#                            ]
#     if len(current_outliers) > 0:
#         print("Data point yang dipertimbangkan sebagai outliers pada feature '{}':".format(i))
#         print(" ")
#         print(current_outliers)
#     else:
#         print("Tidak ada data point yang dipertimbangkan sebagai outliers pada feature '{}'".format(i))
#         print(" ")
#     outliers_counter.update(current_outliers.index.values)