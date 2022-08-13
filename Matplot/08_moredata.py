import matplotlib.pyplot as plt

## COVID-19 백신 종류별 접종 인구
days = [1, 2, 3] # 1일, 2일, 3일
az = [2, 4, 8] # (단위 : 만명) 1일부터 3일까지 아스트라제네카 접종인구
pfizer = [5, 1, 3] # 화이타
moderna = [1, 2, 5] # 모더나

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', ls='-.')

plt.legend(ncol=3) 
