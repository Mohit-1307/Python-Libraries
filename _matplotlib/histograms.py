import matplotlib.pyplot as plt
import numpy as np

"""Histograms -> a visual representation of the distribution of quantitative data.
they group values into bins(intervals) and counts hoe many fall in each range."""

scores = np.random.normal(loc = 80, scale = 10, size = 100)

scores = np.clip(scores, 0, 100)

plt.hist(scores, bins = 10,
         color = '#454745',
         edgecolor = 'black')

plt.title('Exam Scores')

plt.xlabel('Score')

plt.ylabel('No. of Students')

plt.show()