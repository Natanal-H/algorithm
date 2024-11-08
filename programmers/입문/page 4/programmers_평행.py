# 프로그래머스 문제 풀이 - 평행 (120875)

## 문제 정보
# **문제 이름**: 평행
# **문제 번호**: 120875
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120875)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.
# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

## 코드
def slope(a, b):
    return abs(a[1]-b[1])/abs(a[0]-b[0])

def solution(dots):
    arr = [[0,1,2,3],[0,2,1,3],[0,3,1,2]]
    
    for a in arr:
        if slope(dots[a[0]], dots[a[1]]) == slope(dots[a[2]], dots[a[3]]) :
            return 1
    
    return 0
