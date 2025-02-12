# 프로그래머스 문제 풀이 - 점의 위치 구하기 (120841)

## 문제 정보
# **문제 이름**: 점의 위치 구하기
# **문제 번호**: 120841
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120841)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다.
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 
# 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else :
            return 4
    elif dot[1] > 0:
        return 2
    else:
        return 3
