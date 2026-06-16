import pandas as pd
import os

# create a sample DataFRame with column names
data = {
    'Name' : ['alice', 'bob', 'charlie'],
    'Age' : [25,30,35],
    'City' : ['New York', 'Los Angles', 'Chicago']
}

df = pd.DataFrame(data)

data_dir = 'data'

os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")