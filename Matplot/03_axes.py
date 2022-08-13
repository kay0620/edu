import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)
plt.xlabel('X축', color='red', loc='right') # left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top') # top, center, bottom

plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()
