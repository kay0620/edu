#index : 데이터에 접근할 수 있는 주소 값

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
print(df.index)

#인덱스 이름 설정
df.index.name = '지원번호'

#인덱스 초기화
df.reset_index() #기존의 인덱스는 컬럼으로 변경 
df.reset_index(drop=True, inplace = True)

#새로운 컬럼으로 인덱스 설정
df.set_index('이름', inplace=True)

#인덱스 정렬
df.sort_index() #인덱스로 오름차순 정렬
df.sort_index(ascending=False) # 내림차순으로 정렬
