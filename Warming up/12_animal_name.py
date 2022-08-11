import random

animals = {"ㅂㅇㄹ" : "병아리",
"ㅋㄲㄹ" : "코끼리",
"ㅇㄹㅁ" : "얼룩말",
"ㄷㄹㄴ" : "도롱뇽",
"ㅅㅌㄲ" : "산토끼",
"ㅊㅅㅁ" : "청솔모",
"ㄲㅁㄱ" : "까마귀",
"ㄷㄷㅈ" : "두더지",
"ㄷㄹㅈ" : "다람쥐",
"ㄷㅁㅂ" : "도마뱀",
"ㄷㅅㄹ" : "독수리",
"ㄴㄱㄹ" : "너구리",
"ㅎㄹㅇ" : "호랑이",
"ㅋㅃㅅ" : "코뿔소",
"ㄱㄹㄱ" : "기러기",
"ㅇㅅㄹ" : "오소리",
"ㅋㅇㄹ" : "코알라",
"ㄱㄹㄹ" : "고릴라",
"ㅈㄱㅇ" : "재규어",
"ㅂㅇㅇ" : "부엉이"}

print("<<동물 초성 게임>>")

quiz = random.sample(sorted(animals.keys()),10)
# random.choices([*animals.keys()],k=10)

cnt = 0
for i, s in enumerate(quiz):
    answer= input('%d. %s?'%(i+1,s))
    if answer == animals[s]:
        print('correct!!')
        cnt += 1
    else:
        print('wrong!!')
        
print('정답 횟수 : ', cnt)
