'''
입력
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가
공백을 두고 입력된다.(모두 0 ~ 10)

출력
n번째 수를 출력한다.

입력 예시   
2 3 7

출력 예시
1458
'''
a,r,n = map(int,input().split())
s = a
for i in range(1,n,1):
  s = s * r
print(s)