import pandas as pd
df=pd.read_csv('laptop.csv')
new_df=df.dropna()
print(new_df.to_string())