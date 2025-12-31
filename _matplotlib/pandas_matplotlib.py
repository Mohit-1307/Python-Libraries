import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('pokemon.csv')

type_count = df['Type1'].value_counts(ascending = True)

plt.barh(type_count.index, type_count.values, color = '#09e0dd', edgecolor = 'black')

plt.title('No. of Pokemon by Primary Type')

plt.xlabel('Count')

plt.ylabel('Type')

plt.tight_layout()

plt.show()