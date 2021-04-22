'''
입력
30 보다 작은 정수 1개가 입력된다.
(1 ~ 29)

출력
1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.

입력 예시   
9

출력 예시
1 2 X 4 5 X 7 8 X
'''
a = int(input())
for i in range(1,a+1,1):
  if i%10 == 3:
    print('X',end=' ')
  elif i%10 == 6:
    print('X',end=' ')
  elif i%10 == 9:
    print('X',end=' ')
  else:
    print(i,end=' ')