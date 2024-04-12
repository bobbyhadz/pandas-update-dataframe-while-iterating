# Update a Pandas DataFrame while iterating over its rows

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

for index, row in df.iterrows():
    if row['salary'] < 190:
        df.at[index, 'salary'] = 200

#     name  experience  salary
# 0  Alice           1   200.0
# 1  Bobby           3   200.0
# 2   Carl           5   190.3
# 3    Dan           7   205.4
print(df)