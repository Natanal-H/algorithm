# 프로그래머스 문제 풀이 - 정수를 나선형으로 배치하기 (181832)

## 문제 정보
# **문제 이름**: 정수를 나선형으로 배치하기
# **문제 번호**: 181832
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181832)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 양의 정수 n이 매개변수로 주어집니다. 
# n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    cnt = 1 
    y = x = d = 0
    dir_y = [0, 1, 0, -1]
    dir_x = [1, 0, -1, 0]
    
    while cnt <= n**2 :
        answer[y][x] = cnt
        cnt += 1
        
        if y + dir_y[d] < 0 or y + dir_y[d] >= n or x + dir_x[d] < 0 or x + dir_x[d] >= n or answer[y + dir_y[d]][x + dir_x[d]] :
            d = (d + 1) % 4
        
        y += dir_y[d]
        x += dir_x[d]    
        
    return answer
