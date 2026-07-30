import numpy as np

# Multi-Dimensional Array
# 1. 0-Dimensional Array
array = np.array('A')

print(array.ndim)

print(array.shape)

# 2. 1-Dimensional Array
array = np.array(['A', 'B', 'C'])

print(array.ndim)

print(array.shape)

# 3. 2-Dimensional Array
array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F'], 
                  ['G', 'H', 'I']])

print(array.ndim)

# 4. 3-Dimensional Array
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                 [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                 [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]])

print(array.ndim)

print(array.shape)