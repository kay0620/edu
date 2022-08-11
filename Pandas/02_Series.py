#1월 부터 4월까지 평균 온도 데이터 (-20,-10,10,20)
tmp = pd.Series([-20,-10,10,20])
print(tmp) 

print(tmp[0]) #1월의 온도
print(tmp[2]) #3월온도


#인덱스 지정
tmp = pd.Series([-20,-10,10,20], index = ['Jan','Feb','Mar','Apr'])
print(tmp) 

print(tmp['Jan']) #1월의 온도
print(tmp['Mar']) #3월온도
print(tmp['Jun']) #6월온도 #error
