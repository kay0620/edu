#계산 가능한 데이터에 대해 Column 별로 데이터의 갯수, 평균, 표준편차, 최소/최대값 등의 정보를 보여줌
df.describe()

#컬럼 정보
df.info()

df.head() # 처음 5개의 row 를 가져옴
df.head(7) # 처음 7개의 row 를 가져옴
df.tail() # 마지막 5개 row 를 가져옴
df.tail(3) # 마지막 3개 row 를 가져옴

df.values #값확인
df.index #인덱스 확인
df.columns #컬럼 확인
df.shape # row, column 개수 확인

# Series 확인
df['키'].describe()

df['키'].min()
df['키'].max()
df['키'].nlargest(3) # 키 큰 사람 순서대로 3명 데이터
df['키'].mean()
df['키'].sum()

df['SW특기'].count()

df['학교'].unique() #북산고, 능남고
df['학교'].nunique() #학교 개수 2
