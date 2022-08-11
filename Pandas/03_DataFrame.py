#사전 자료구조를 통해서 데이터 생성
data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
print(data['이름'])
print(data['키'])


#데이터프레임 생성
df = pd.DataFrame(data)
print(df) #데이터 확인
print(df['이름']) #인덱스와 이름 같이 출력
print(df['키'])
print(df[['이름','키']] )


#index 지정
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])


#특정 column 지정하여 객체 생성
df = pd.DataFrame(data, columns=['이름', '학교', '키'])
