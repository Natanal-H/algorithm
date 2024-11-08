# 프로그래머스 문제 풀이 - 짝수의 합 (120831)

## 문제 정보
# **문제 이름**: 짝수의 합
# **문제 번호**: 120831
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120831)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

## 코드
def solution(n):
    return sum([i for i in range(2, n+1, 2)])
