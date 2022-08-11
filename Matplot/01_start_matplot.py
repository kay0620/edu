#설치
# pip install matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]
plt.plot(x, y)
plt.show()

#title 
plt.plot(x, y)
plt.title('Line Graph')

plt.plot(x, y)
plt.title('꺾은선 그래프') #error

#한글폰트 설정
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

plt.plot(x, y)
plt.title('꺾은선 그래프')
