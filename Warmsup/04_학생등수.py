score_list = []

for i in range(5):
    score = int(input('점수를 입력하세요 : '))
    score_list.append(score)
    
score_list.sort(reverse=True)

print('\n\n<< 등수 출력 >> ')
rank = 1
for s in score_list:
    print('{}점 학생 : {}등'.format(s, rank))
    rank += 1
