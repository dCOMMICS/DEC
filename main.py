import pandas as pd

# the excel file importation

df = pd.read_csv('/big_flight_operations_dirty_1M.csv', low_memory= False)

# 

print(df)
