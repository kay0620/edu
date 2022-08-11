# 비밀번호 자동 생성
# 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성

url = input('사이트 입력 : ')
string = url.replace('http://','')
string = string[:string.index('.')]

new_passwd = string[:3] + str(len(string)) + str(string.count('e')) + '!'
print("새 비밀번호는 {} 입니다.".format(new_passwd))
