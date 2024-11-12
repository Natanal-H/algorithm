# 프로그래머스 문제 풀이 - 겹치는 선분의 길이 (120876)

## 문제 정보
# **문제 이름**: 겹치는 선분의 길이
# **문제 번호**: 120876
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120876)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
# 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(lines):
    arr = [[0 for _ in range(3)] for _ in range(201)]

    for i in range(3):    
        for j in range(lines[i][0]+100, lines[i][1]+100):
            arr[j][i] = 1
            
    return sum([1 if sum(arr[i]) >= 2 else 0 for i in range(201)])
