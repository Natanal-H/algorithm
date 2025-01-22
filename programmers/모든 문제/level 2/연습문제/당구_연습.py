# 프로그래머스 문제 풀이 - 당구 연습 (169198)

## 문제 정보
# **문제 이름**: 당구 연습
# **문제 번호**: 169198
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/169198)
# **풀이 날짜** : 2025-01-22

## 문제 
# 문제 설명 :
# 당구대의 가로 길이 m, 세로 길이 n과 머쓱이가 쳐야 하는 공이 놓인 위치 좌표를 나타내는 두 정수 startX, startY, 그리고 매 회마다 목표로 해야하는 공들의 위치 좌표를 나타내는 정수 쌍들이 들어있는 2차원 정수배열 balls가 주어집니다. 
# "원쿠션" 연습을 위해 머쓱이가 공을 적어도 벽에 한 번은 맞춘 후 목표 공에 맞힌다고 할 때, 각 회마다 머쓱이가 친 공이 굴러간 거리의 최솟값의 제곱을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## 코드
MAX = 1e9

def calc(x, y):
    return x ** 2 + y ** 2

def solution(m, n, x, y, balls):
    answer = []
    
    for ball in balls:
        A, B = ball[0] + x, ball[1] + y
        C, D = ball[0] - x, ball[1] - y
        
        a = calc(A, D)
        b = calc(2 * m - A, D)
        
        if D == 0:
            if ball[0] < x : a = MAX
            else : b = MAX
            
        c = calc(C, B)
        d = calc(C, 2 * n - B)
        
        if C == 0:
            if ball[1] < y : c = MAX
            else : d = MAX
        
        answer.append(min(min(a,b), min(c,d)))
    
    return answer
