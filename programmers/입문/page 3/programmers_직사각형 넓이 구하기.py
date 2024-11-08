# 프로그래머스 문제 풀이 - 직사각형 넓이 구하기 (120860)

## 문제 정보
# **문제 이름**: 직사각형 넓이 구하기
# **문제 번호**: 120860
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120860)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
# 직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열 dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(dots):
    x = sorted([dots[i][0] for i in range(4)])
    y = sorted([dots[i][1] for i in range(4)])
    return (x[2]-x[0]) * (y[2]-y[0])
