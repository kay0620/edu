import pandas as pd
df = pd.read_excel('score.xlsx')

import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2, figsize=(15, 10)) 

fig.suptitle('여러 그래프')

# 첫 번째 그래프
axs[0, 0].bar(df['이름'], df['국어'], label='국어점수') # 데이터 설정
axs[0, 0].set_title('첫 번째 그래프') # 제목
axs[0, 0].legend() # 범례
axs[0, 0].set(xlabel='이름', ylabel='점수') # x, y 축 label
axs[0, 0].set_facecolor('lightyellow') # 전면 색
axs[0, 0].grid(linestyle='--', linewidth=0.5)

# 두 번째 그래프
axs[0, 1].plot(df['이름'], df['수학'], label='수학')
axs[0, 1].plot(df['이름'], df['영어'], label='영어')
axs[0, 1].legend()

# 세 번째 그래프
axs[1, 0].barh(df['이름'], df['키'])

# 네 번째 그래프
axs[1, 1].plot(df['이름'], df['사회'], color='green', alpha=0.5)

plt.show()
