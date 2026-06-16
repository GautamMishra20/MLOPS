import pandas as pd
import os

# create a sample DataFRame with column names
data = {
    'Name' : ['alice', 'bob', 'charlie'],
    'Age' : [25,30,35],
    'City' : ['New York', 'Los Angles', 'Chicago']
}

df = pd.DataFrame(data)

# adding new row to df for version 2
new_row = {
    'Name' : 'Yatharth',
    'Age' : 50,
    'City' : 'Gurgaon'
}
df.loc[len(df.index)] = new_row

# Adding data to the saved data file for the version 3
new_row2 = {
    'Name' : 'Gautam Mishra',
    'Age' : 23,
    'City' : 'Madhubani Bihar'
}
df.loc[len(df.index)] = new_row2

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")