'''
3항연산

입력
3개의 정수가 공백으로 구분되어 입력된다.
-2147483648 ~ +2147483648

출력
가장 작은 값을 출력한다.

입력 예시   
3 -1 5

출력 예시
-1
'''
a,b,c = map(int,input().split())
print((a if a <= b else b) if ((a if a <= b else b)< c) else c)