import pandas as pd
df = pd.read_excel('score.xlsx')

import matplotlib.pyplot as plt

plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])

plt.title("학생별 영어 수학 성적")
plt.grid(axis='y', color='purple', alpha=0.5, linestyle='--', linewidth=2)
