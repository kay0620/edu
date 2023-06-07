print('<답안 채점 프로그램>\n')

print('정답을 입력하세요:')
t_answer = []
for i in range(10):
    a = input('%d번 정답'%(i+1))
    t_answer.append(a)
    
print('='*20)
print('<채점결과>')

with open('st_answer.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    
    for no, i in enumerate(lines):
        i = i.replace('\n','')
        st = i.split(',')
        
        print()
        count = 0
        for i, e in enumerate(t_answer):
            if e == st[i]:
                count += 1
        print(f'{no+1}번 학생 점수 {count * 10}점')
