# 프로그래머스 문제 풀이 - 제곱수 판별하기 (120909)

## 문제 정보
# **문제 이름**: 제곱수 판별하기
# **문제 번호**: 120909
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120909)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    return 2 if (n**(1/2)) % 1 else 1
