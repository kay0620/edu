#url = 'http://naver.com'
url = input('사이트 주소를 입력하세요 : ')

# http:// 삭제
# url = url[len('http://'):]
url = url.replace('http://','')

# 첫번째 점부터 뒤에 문자 제거
idx = url.index('.')
url = url[0:idx]

new_passwd = url[:3] + str(len(url)) + str(url.count('e')) + '!'
print(f'새 비밀번호는 {new_passwd} 입니다')
