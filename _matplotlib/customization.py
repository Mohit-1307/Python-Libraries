import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])

y1 = np.array([15, 25, 30, 20])

y2 = np.array([17, 23, 38, 5])

y3 = np.array([13, 15, 20, 30])

line_style = dict(marker = '.',
                  markersize = 20,
                  linestyle = 'solid',
                  linewidth = 3)

plt.plot(x, y1, color = "#27F56F", markerfacecolor = "#27F565", markeredgecolor = "#27F565", ** line_style)

plt.plot(x, y2, color = "#CC27F5", markerfacecolor = "#BE27F5", markeredgecolor = "#CF27F5", ** line_style)

plt.plot(x, y3, color = "#27A3F5", markerfacecolor = '#27D3F5', markeredgecolor = '#27D3F5', ** line_style)

plt.show()