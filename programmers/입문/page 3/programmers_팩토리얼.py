# 프로그래머스 문제 풀이 - 팩토리얼 (120848)

## 문제 정보
# **문제 이름**: 팩토리얼
# **문제 번호**: 120848
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120848)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
# 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
# i! ≤ n

## 코드
def solution(n):
    i = 1
    ret = 1
    
    while True:
        if ret > n :
            return i - 1
        i += 1
        ret *= i
    
