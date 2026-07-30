import pandas as pd

"""Series -> a pandas 1-dimensional labeled array that can hold any data type.
think of it like a single column in a spreadsheet(1-dimensional)."""

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e']) # default 1, 2, 3...

print(series)

print(series.loc['a'])

series.loc['a'] = 200

print(series)

print(series.iloc[0])

print(series[series >= 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)

print(series)

print(series.loc['Day 3'])

series.loc['Day 2'] += 500

print(series)

print(series[series < 2000])