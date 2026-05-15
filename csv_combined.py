#!/usr/bin/env/python3

# import modules
# pip install pandas
import os
import pandas as pd

# master dataframe
master_df = pd.DataFrame()

# reads and merges csv files from current working directory
for file in os.listdir(getcwd()):
          if file.endswith('.csv'):
                    master_df.append(pd.read_csv(file))

# saves merged csv file to current working directory
master_df.to_csv('<Final CSV.csv', index=False)
