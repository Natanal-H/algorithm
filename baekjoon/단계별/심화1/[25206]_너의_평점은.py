# ------------------------------------------------------
# 문제 번호 : [25206] 너의 평점은
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/25206
# 난이도 : X
# 분류 : 수학, 구현, 문자열
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 전공평점을 계산해주는 프로그램을 작성해보자.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.

# 코드
grade = {"A+": 4.5, "A0":4.0,
         "B+": 3.5, "B0":3.0,
         "C+": 2.5, "C0":2.0,
         "D+": 1.5, "D0":1.0,
         "F": 0}

sum_point = 0
sum_gp = 0

while True:
    try:
        S, P, G = input().split()
        if G == 'P' : continue
        sum_point += float(P)
        sum_gp += float(P) * grade[G]
    except EOFError:
        break
    
print(sum_gp/sum_point)
