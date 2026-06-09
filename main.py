import pandas as pd
import numpy as np
import re 

# # the excel file importation

df = pd.read_csv('big_flight_operations_dirty_1M.csv', low_memory= False)

# 
df ['airline'] = df ['airline'].str.strip().str.title()

# FLIGHT TYPE 

df['flight_type'] = df['flight_type'].str.strip().str.lower()
df['flight_type'] = df['flight_type'].replace({
    'intl': 'international',
    'dom': 'domestic'
})

#  SOMETHINGS TO BE DELETED BELOW THIS AND OTHERS ARE FOR TESTING PURPOSES ONLY AND LEFT.
# print(df.head(200))

# print(df.columns.tolist())
# print(df.dtypes)
# print(df.isnull().sum())




# Full diagnostic

# THIS IS WHAT I USE TO CHECK THE DATASET AND SEE WHAT I AM DEALING WITH, I CAN ALSO USE THIS TO CHECK THE DATASET AFTER CLEANING TO SEE IF THERE ARE ANY CHANGES OR IMPROVEMENTS.
# print("=== SHAPE ===")
# print(df.shape)

# print("\n=== COLUMNS & DTYPES ===")
# print(df.dtypes)

# print("\n=== NULL COUNTS ===")
# print(df.isnull().sum())

# print("\n=== FIRST 10 ROWS ===")
# print(df.head(10))

# print("\n=== SAMPLE OF UNIQUE VALUES PER COLUMN ===")
# for col in df.columns:
#     print(f"\n-- {col} --")
#     print(df[col].unique()[:10])