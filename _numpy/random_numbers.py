import numpy as np

rng = np.random.default_rng(seed = 1) # seed is used to produce same result

print(rng.integers(low = 1, high = 7, size = (3, 2)))

np.random.seed(seed = 1) 

print(np.random.uniform(low = -1, high = 1, size = (3, 2)))

array = np.array([1, 2, 3, 4 , 5])

np.random.shuffle(array)

print(array)

rng = np.random.default_rng()

fruits = np.array(['apple', 'orange', 'banana', 'coconut', 'pineapple'])

fruit = rng.choice(fruits)

print(fruit)

fruits = rng.choice(fruits, size = (3, 3))

print(fruits)