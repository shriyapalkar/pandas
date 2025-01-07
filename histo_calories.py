import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data-1.csv')

df["Calories"].plot(kind = 'hist')

plt.show()