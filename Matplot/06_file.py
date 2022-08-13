import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)

#dpi : 파일에 저장할 그림의 해상도
plt.savefig('graph.png', dpi=100) 
