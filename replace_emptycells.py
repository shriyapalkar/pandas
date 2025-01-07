import pandas as pd

df = pd.read_csv('laptop.csv')

df.fillna(130,inplace=True)