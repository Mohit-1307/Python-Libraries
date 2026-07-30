import numpy as np

scores1 = np.array([91, 55, 100, 73, 82, 64])

scores2 = np.array([81, 32, 53, 100, 29, 64])

print(scores1 == scores2)

print(scores1 == 100)

print(scores1 > 100)

print(scores1 < 100)

scores1[scores1 < 60] = 0

print(scores1)