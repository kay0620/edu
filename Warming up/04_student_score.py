#학생의 점수를 5개 입력받아 점수와 등수를 출력

score_list=[]
for i in range(5):
    score = int(input("점수를 입력하세요:"))
    score_list.append(score)
    
for s in score_list:
    rank = 1
    for i in score_list:
        if s < i:
            rank = rank +1

    print(s, "등수는 ", rank , "등입니다")
