import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y, marker='o')

for idx, txt in enumerate(y):
    plt.text(x[idx], y[idx] + 0.3, txt, ha='center', color='blue')
