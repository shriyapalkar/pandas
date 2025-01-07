import pandas as pd
df=pd.read_csv('laptop.csv')
print(df.head(10))

# Print the last 5 rows of the DataFrame:
print(df.tail())
print(df.info())