import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 8]

# linewidth : 선두께
# linestyle : 선스타일
# color : 선색깔
# marker : 마커모양
# markersize : 마커 크기
# markeredgecolor : 마커 테두리 색
# markerfacecolor : 마커 색깔
# alpha : 투명도
plt.plot(x, y, linewidth=5, linestyle=':', color='pink',
         marker='o', markersize=20, markeredgecolor='red', 
         markerfacecolor='yellow', alpha=0.2) 

# 포맷으로 설정
plt.plot(x, y, 'ro--') # color, marker, linestyle

# figsize : 그래프 크기
# facecolor : 전경색
# dpi : 해상도
plt.figure(figsize=(10, 5), facecolor='yellow', dpi=200)
plt.plot(x, y)

#그리드 설정
# axis : 축
# color : 색깔
# alpha : 투명도
# linestyle : 선 스타일
plt.grid(axis='y', color='purple', alpha=0.5, linestyle='--')
plt.plot(x, y)
