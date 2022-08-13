import matplotlib.pyplot as plt

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
colors = ['b', 'g', 'r', 'c', 'm', 'y']

#autopct : 비율 표시
#startangle : 시작 각도
#counterclock : 반시계방향으로 진행
#explode : 차트 간격
plt.pie(values, labels=labels, autopct='%.1f%%', 
        startangle=90, counterclock=False, 
        explode=[0.2, 0.1, 0, 0, 0, 0],
        colors=colors
       )
plt.show()

#도넛차트
wedgeprops={'width':0.6, 'edgecolor':'w', 'linewidth':2}
plt.pie(values, labels=labels, autopct='%.1f%%', 
        startangle=90, counterclock=False, colors=colors, 
        wedgeprops=wedgeprops)
plt.show()

#10 이하 텍스트는 출력 안되도록 수정
def custom_autopct(pct):
  return '{:.0f}%'.format(pct) if pct >= 10 else ''

# pctdistance : 퍼센트들의 거리 설정
plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, 
        counterclock=False, colors=colors, wedgeprops=wedgeprops, 
        pctdistance=0.7)
plt.show()
