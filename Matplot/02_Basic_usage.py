import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.title('Line Graph')
plt.show()


#한글폰트 설정
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows #HYGungSo-Bold
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15 
matplotlib.rcParams['axes.unicode_minus'] = False  

#한글을 입력한 경우
plt.plot(x, y)
plt.title('꺾은선 그래프') 

#-값을 입력한 경우 
plt.plot([-1, 0, 1], [-5, -1, 2])
