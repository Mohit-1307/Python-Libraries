import pandas as pd

"""Data Cleaning -> the process of fixing/removing:
                    incomplete, incorrect, or irrelevant data.
                    ~75% of work done with pandas is data cleaning."""

df = pd.read_csv('pokemon.csv')

# 1. Drop Irrelevant Columns
df = df.drop(columns = ['Legendary', "No"])

print(df)

# 2. Handle Missing Data
df = df.dropna(subset = ['Type2'])

print(df.to_string())

df = df.fillna({'Type2': 'None'})

print(df.to_string())

# 3. Fix Inconsistent Values
df['Type1'] = df['Type1'].replace({'Grass': 'GRASS',
                                   'Fire': 'FIRE',
                                   'Water': 'WATER'})

print(df.to_string())

# 4. Standardize Text
df['Name'] = df['Name'].str.lower()

print(df.to_string())

# 5. Fix Data Types
df['Legendary'] = df['Legendary'].astype(bool)

print(df.to_string())

# 6. Remove Duplicate Values
df = df.drop_duplicates()

print(df.to_string())