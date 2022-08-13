import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y, label='범례') 
#case 1
#plt.legend(loc='lower right')
#case 2
plt.legend(loc=(0.7, 0.8)) # x축, y축 (0~1 사이)
