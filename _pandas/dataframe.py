import pandas as pd

"""DataFrame -> a tabular data structure with rows and columns.
think of it like a spreadsheet or SQL table, or a dictionary of Series objects(2-dimensional)."""

data = {
    'Name': ['Spongebob', 'Patrick', 'Squidward'],
    'Age': [30, 35, 50],
}

df = pd.DataFrame(data, index = ['Employee 1', 'Employee 2', 'Employee 3'])

print(df)

print(df.loc['Employee 2'])

print(df.iloc[0])

# Add A New Column
df['Job'] = ['Cook', 'N/A', 'Cashier']

# Add New Rows
df.loc['Employee 4'] = ['Sandy', 32, 'Scientist']
new_rows = pd.DataFrame([{'Name': 'Sandy', 'Age': 28, 'Job': 'Engineer'},
                        {'Name': 'Eugene', 'Age': 60, 'Job': 'Manager'}],
                        index = ['Employee 4', 'Employee 5'])

df = pd.concat([df, new_rows])

print(df)