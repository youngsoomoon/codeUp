"""
입력
2개의 정수가 공백을 두고 입력된다.
-2147483648 ~ +2147483647

출력
두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.

입력 예시   
3 5

출력 예시
1
"""
a,b = map(int,input().split())
print(a & b)