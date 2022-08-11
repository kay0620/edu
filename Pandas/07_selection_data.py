df.columns
df.columns[0] #0번째 컬럼의 이름이 출력
df.columns[2] #2번째 컬럼의 키가 출력

df[df.columns[0]] # df['이름'] 과 동일한 동작
df[df.columns[-1]] # 맨 끝에 있는 값을 가져옴

#slicing
df['영어'][0:5] # 0~4 까지 영어 점수 데이터 가져옴
df[['이름', '키']][:3] # 처음 3명의 이름, 키 정보를 가져옴

#loc : 이름을 이용하여 row, column 선택
df.loc['1번'] # index 1번에 해당하는 전체 데이터
df.loc['5번'] # index 5번에 해당하는 전체 데이터
df.loc['1번', '국어'] # index 1번에 해당하는 국어 데이터
df.loc[['1번', '2번'], '영어'] # index 1번, 2번에 해당하는 영어 데이터
df.loc[['1번', '2번'], ['영어', '수학']] # index 1번, 2번에 해당하는 영어, 수학 데이터
df.loc['1번':'5번', '국어':'사회'] # index 1번부터 5번까지, 국어부터 사회까지 데이터

#iloc : 숫자를 이용하여 row, column 선택
df.iloc[0] # 0번째 위치의 데이터
df.iloc[4] # 4번째 위치의 데이터 강백호 학생의 모든 데이터
df.iloc[0:5] # 0 ~ 4번째 위치의 데이터 5포함안됨
df.iloc[0, 1] # 0번째 위치의 1번째(학교) 데이터
df.iloc[4, 2] # 5번 학생의 키 데이터 (4번째 위치의 2번째(키) 데이터)
df.iloc[[0, 1], 2] # 0, 1번째 위치의 학생의 2번째(키) 데이터
df.iloc[[0, 1], [3, 4]] # 0, 1 번째 위치의 학생의 3, 4 번째 데이터 (국어, 영어)
df.iloc[0:5, 3:8] # 0 ~ 4 번째 위치의 학생 중에서, 3 ~ 7 번째 데이터 (국어:사회)

#조건
df['키'] >= 185 # 학생들의 키가 185 이상인지 여부를 True / False
filt = (df['키'] >= 185)
df[filt] #185이상
df[~filt] #185미만
df[df['키'] >= 185]
df.loc[df['키'] >= 185, '수학'] # 키가 185 이상인 학생들의 수학 데이터
df.loc[df['키'] >= 185, ['이름', '수학', '과학']]
df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')] # 키가 185 이상인 북산고 학생 데이터
df.loc[(df['키'] < 170) | (df['키'] > 200)] # 키가 170 보다 작거나, 200 보다 큰 학생 데이터

ilt = df['이름'].str.startswith('송') # '송'씨 성을 가진 사람 스탈스위드
df[filt]
filt = df['이름'].str.contains('태') # 이름에 '태'가 들어가는 사람 컨테인스
df[filt]

langs = ["Python", "Java"]
filt = df['SW특기'].isin(langs) # SW특기가 Python 이거나 Java 인 사람
filt = df['SW특기'].str.lower().isin(langs) #PYTHON도 검색
df[filt]

filt = df['SW특기'].str.contains('Java')
df[filt] ## Nan 데이터 때문에 error 발생

df['SW특기'].str.lower()
df['SW특기'].str.lower().isin(langs)

df['SW특기'].str.contains('Java') #4번 5번 NaN 데이터 필터링할때 처리가 안되서 오류가 남
df['SW특기'].str.contains('Java', na=True) # NaN 데이터에 대해서 True 로 설정
df['SW특기'].str.contains('Java', na=False) # NaN 데이터에 대해서 False 로 설정

filt = df['SW특기'].str.contains('Java', na=False)
df[filt]
