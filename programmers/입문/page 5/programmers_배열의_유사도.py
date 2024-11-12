# 프로그래머스 문제 풀이 - 배열의 유사도 (120903)

## 문제 정보
# **문제 이름**: 배열의 유사도
# **문제 번호**: 120903
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120903)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(s1, s2):
    return len(set(s1).intersection(set(s2)))
