import pandas as pd
df = pd.read_excel('score.xlsx')
df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]

import matplotlib.pyplot as plt

plt.figure(figsize=(7, 7))

sizes = df['학년'] *100
# c : 색깔 분포
# cmap : color map
# alpha : 투명도
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3)

plt.xlabel('영어 점수')
plt.ylabel('수학 점수')

# shrink : colorbar 크기
# orientation : 방향
plt.colorbar(ticks=[1, 2, 3], label='학년', shrink=0.5, orientation='horizontal')
plt.show()
