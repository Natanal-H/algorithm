# ------------------------------------------------------
# 문제 번호 : [25304] 영수증
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/25304
# 난이도 : X
# 분류 : 수학, 구현, 사칙연산
# 날짜 : 2024-10-29
# ------------------------------------------------------

# 문제 설명 :
# 영수증에 적힌, 구매한 각 물건의 가격과 개수, 구매한 물건들의 총 금액을 보고, 
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

# 코드
x = int(input())
n = int(input())
count = 0

for i in range(n) :
    a, b = map(int, input().split())
    count += a * b
    
if x == count:
    print("Yes")
else :
    print("No")
