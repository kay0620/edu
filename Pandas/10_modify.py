import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')

#컬럼 수정
df['학교'].replace({'북산고':'상북고'}, inplace=True)

#대소문자로 변경
df['SW특기'] = df['SW특기'].str.lower()
df['SW특기'] = df['SW특기'].str.upper()

#데이터 내용 수정
df['학교'] = df['학교'] + '등학교' 

#column 추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df['결과'] = 'Fail' # 결과 Column 을 추가하고 전체 데이터는 Fail 로 초기화
df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터에 대해서 결과를 Pass 로 업데이트 

#column 삭제
df.drop(columns=['총합']) # 총합 Column 을 삭제
df.drop(columns=['국어', '영어', '수학']) # 국어, 영어, 수학 Column 을 삭제

#row 삭제
df.drop(index='4번') # 4번 학생 데이터 row 를 삭제
filt = df['수학'] < 80 # 수학 점수 80 점 미만 학생 필터링
df.drop(index=df[filt].index)

#row 추가
df.loc['9번'] = ['이정환', '해남고등학교', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, 'Pass'] 

#cell 수정
df.loc['4번', 'SW특기'] = 'Python' # 4번 학생의 SW특기 데이터를 Python 으로 변경
df.loc['5번', ['학교', 'SW특기']] = ['능남고등학교', 'C']

#column 순서변경
df = df[['결과', '이름', '학교','키','국어','영어','수학','과학','사회','SW특기']]
cols = list(df.columns)
df = df[[cols[-1]] + cols[0:-1]] 

#column 이름변경
df = df[['결과', '이름', '학교']]
df.columns = ['Result', 'Name', 'School']

