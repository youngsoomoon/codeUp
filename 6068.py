'''
입력
정수(0 ~ 100) 1개가 입력된다.

출력
평가 결과를 출력한다.

입력 예시   
73

출력 예시
B
'''
a = int(input())
if a >= 90 :
  print('A')
elif a >= 70 :
  print('B')
elif a >= 40:
  print('C')
else :
  print('D')