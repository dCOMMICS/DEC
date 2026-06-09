# import pandas as pd

# # the excel file importation

# df = pd.read_csv('big_flight_operations_dirty_1M.csv', low_memory= False)

# # 

# print(df.head(200))

# print(df.columns.tolist())
# print(df.dtypes)
# print(df.isnull().sum())


import pandas as pd

df = pd.read_csv('big_flight_operations_dirty_1M.csv', low_memory=False)

# Full diagnostic
print("=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS & DTYPES ===")
print(df.dtypes)

print("\n=== NULL COUNTS ===")
print(df.isnull().sum())

print("\n=== FIRST 10 ROWS ===")
print(df.head(10))

print("\n=== SAMPLE OF UNIQUE VALUES PER COLUMN ===")
for col in df.columns:
    print(f"\n-- {col} --")
    print(df[col].unique()[:10])