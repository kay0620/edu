import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')

df.sort_values('키') # 키 기준으로 오름차순 정렬
df.sort_values('키', ascending=False) # 키 기준으로 내림차순 정렬 키가 큰 학생부터 어센딩

df.sort_values(['수학', '영어']) # 수학, 영어 점수 기준으로 오름차순
df.sort_values(['수학', '영어'], ascending=False) # 수학, 영어 점수 기준으로 내림차순
df.sort_values(['수학', '영어'], ascending=[True, False]) # 수학 점수는 오름차순으로, 영어 점수는 내림차순으로 정렬

#하나의 데이터만 보고 싶다면
df['키'].sort_values()
df['키'].sort_values(ascending=False)
df.sort_index()
df.sort_index(ascending=False)

