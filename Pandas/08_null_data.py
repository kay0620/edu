import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')

#결측치 : 비어있는 데이터 
df.fillna('') # NaN 데이터를 빈 칸으로 채움
df.fillna('없음')

import numpy as np 
df['학교'] = np.nan # 학교 데이터 전체를 NaN 으로 채움
df.fillna('모름')

# 일부데이터만 채우기
df = pd.read_excel('score.xlsx', index_col='지원번호')
df['SW특기'].fillna('확인 중', inplace=True) 

# 비어있는 데이터 삭제하기
df = pd.read_excel('score.xlsx', index_col='지원번호')
df.dropna() 
df.dropna(axis='index', how='any') # NaN 이 하나라도 있는 row 삭제

df = pd.read_excel('score.xlsx', index_col='지원번호')
df.dropna(axis='columns') # NaN 이 하나라도 있는 column 삭제 

df['학교'] = np.nan
df.dropna(axis='columns', how='all') # 데이터 전체가 NaN 인 경우에만 Column 삭제

