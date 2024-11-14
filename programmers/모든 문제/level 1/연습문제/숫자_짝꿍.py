# 프로그래머스 문제 풀이 - 숫자 짝꿍 (131128)

## 문제 정보
# **문제 이름**: 숫자 짝꿍
# **문제 번호**: 131128
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/131128)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다
# (단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다.
# X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

## 코드
def solution(X, Y):
    X = sorted(list(X), reverse=True)
    Y = sorted(list(Y), reverse=True)
    answer = ''
    x, y = 0, 0
    
    while True :
        if X[x] == Y[y] :
            answer += X[x]
            x += 1
            y += 1
        elif X[x] < Y[y] :
            y += 1
        else :
            x += 1
            
        if x == len(X) or y == len(Y) : break
            
    if answer == '' : return '-1'
    if answer.count('0') == len(answer): return '0'
    return answer
