maxnum = int(input('몇주차까지 만드시겠습니까? '))

for n in range(1,maxnum+1):
    file_name = '{}주차.txt'.format(n)

    with open(file_name,'w',encoding='utf-8') as file:
        file.write('- {} 주차 주간보고 - \n'.format(n))
        file.write('부서 : \n')
        file.write('이름 : \n')
        file.write('업무 요약 : \n')
