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

# PASSENGERS COLUMN

def clean_numeric(val):
    if pd.isna(val):
        return np.nan
    val = str(val).lower().strip()
    # Remove 'kg' or other units
    val = re.sub(r'[a-zA-Z]', '', val).strip()
    # Convert text numbers
    text_map = {'one hundred': '100', 'two hundred': '200'}
    for k, v in text_map.items():
        val = val.replace(k, v)
    try:
        return float(val)
    except:
        return np.nan

df['passengers'] = df['passengers'].apply(clean_numeric)
df['cargo_kg'] = df['cargo_kg'].apply(clean_numeric)

# CONVERTING FLIGHT DATE TO DATETIME

df['flight_date'] = pd.to_datetime(df['flight_date'], dayfirst=False, errors='coerce')

# DROPPING DUPLICATES
df = df.drop_duplicates()

# CHECKING THE CLEANED DATASET
print("THIS IS CLEAN")
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df.head(10))

# LAST PART 
df.to_csv('big_flight_operations_clean.csv', index=False)
print("\nSaved to big_flight_operations_clean.csv")

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


print(df.isnull().sum())
print("\n-- flight_type unique --")
print(df['flight_type'].unique())
print("\n-- airline unique --")
print(df['airline'].unique())
print("\n-- passengers sample --")
print(df['passengers'].head(10))
print("\n-- cargo_kg sample --")
print(df['cargo_kg'].head(10))
print("\n-- flight_date sample --")
print(df['flight_date'].head(10))