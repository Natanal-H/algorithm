# ------------------------------------------------------
# 문제 번호 : [10430] 나머지
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10430
# 난이도 : X
# 분류 : 수학, 구현, 사칙연산
# 날짜 : 2024-10-29
# ------------------------------------------------------

# 문제 설명 :
# 세 수 A, B, C가 주어졌을 때,
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

# 코드
A,B,C=map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
