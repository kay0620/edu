import matplotlib.pyplot as plt

labels = ['강백호', '서태웅', '정대만'] # 이름
values = [190, 187, 184] # 키

bar = plt.bar(labels, values, color='y')
plt.ylim(175,195) #y축 데이터 값 범위 설정
plt.yticks(rotation = 45)

ticks = ['1번학생', '2번학생', '3번학생']
plt.xticks(labels, ticks, rotation=90)

#pattern
bar[0].set_hatch('/') # ////
bar[1].set_hatch('x') # xxxx
bar[2].set_hatch('..') # ...

#text
for idx, rect in enumerate(bar): 
  plt.text(idx, rect.get_height() + 0.5, values[idx], 
             ha='center', color='blue')
