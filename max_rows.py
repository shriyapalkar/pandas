import pandas as pd

df = pd.read_csv('laptop.csv')
#max_rows.py
print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 500
#df = pd.read_csv('laptop.csv')
print(df)