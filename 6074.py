'''
입력
영문자 1개가 입력된다.
(a ~ z)

출력
a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

입력 예시   
f

출력 예시
a b c d e f
'''
i= ord(input())
a = ord('a')
while i>=a :
  print(chr(a),end=' ')
  a += 1