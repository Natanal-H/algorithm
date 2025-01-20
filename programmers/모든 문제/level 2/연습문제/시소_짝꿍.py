# 프로그래머스 문제 풀이 - 시소 짝꿍 (152996)

## 문제 정보
# **문제 이름**: 시소 짝꿍
# **문제 번호**: 152996
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/152996)
# **풀이 날짜** : 2025-01-20

## 문제 
# 문제 설명 :
# 어느 공원 놀이터에는 시소가 하나 설치되어 있습니다. 이 시소는 중심으로부터 2(m), 3(m), 4(m) 거리의 지점에 좌석이 하나씩 있습니다.
# 이 시소를 두 명이 마주 보고 탄다고 할 때, 시소가 평형인 상태에서 각각에 의해 시소에 걸리는 토크의 크기가 서로 상쇄되어 완전한 균형을 이룰 수 있다면 그 두 사람을 시소 짝꿍이라고 합니다. 즉, 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같다면 시소 짝꿍이라고 할 수 있습니다.
#사람들의 몸무게 목록 weights이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하여 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(w):
    answer = 0
    d = {}
    
    for i in range(len(w)):
        if w[i] not in d: d[w[i]] = 1
        else : d[w[i]] += 1
        
    for i in range(100, 1001):
        if i in d :
            if d[i] > 1 : 
                answer += d[i] * (d[i] - 1) // 2
            
            n = i * 2
            if n in d : answer += d[i] * d[n]
            
            n = i * 1.5
            if n % 1 == 0 and n in d : answer += d[i] * d[n]
            
            n = i * 4 / 3
            if n % 1 == 0 and n in d : answer += d[i] * d[n]
                
    return answer
