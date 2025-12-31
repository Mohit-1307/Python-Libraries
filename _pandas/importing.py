import pandas as pd

df = pd.read_csv('pokemon.csv', index_col = 'Name')

print(df.to_string())


# Selection By Column
print(df['Name'].to_string())

print(df['Height'].to_string())

print(df['Weight'].to_string())

print(df[['Name', 'Height', 'Weight']].to_string())


# Selection By Row
print(df.loc['Charizard':'Blastoise', ['Height', 'Weight']])

print(df.iloc[0:11:2, 0:3])

pokemon = input('Enter a pokemon name: ')

try:
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found')