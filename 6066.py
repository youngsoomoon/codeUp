'''
입력
3개의 정수(a, b, c)가 공백을 두고 입력된다.
0 <= a,b,c <= 2147483647

출력
입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.

입력 예시   
1 2 8

출력 예시
odd
even
even
'''
a,b,c = map(int,input().split())
if a%2 == 0:
  print("even")
else:
  print("odd")
if b%2 == 0:
  print("even")
else:
  print("odd")
if c%2 == 0:
  print("even")
else:
  print("odd")