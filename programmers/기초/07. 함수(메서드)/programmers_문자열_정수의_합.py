# 프로그래머스 문제 풀이 - 문자열 정수의 합 (181856)

## 문제 정보
# **문제 이름**: 문자열 정수의 합
# **문제 번호**: 181856
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181856)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_str):
    return sum([int(s) for s in num_str])
