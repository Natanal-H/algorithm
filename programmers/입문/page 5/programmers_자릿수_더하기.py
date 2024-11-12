# 프로그래머스 문제 풀이 - 자릿수 더하기 (120906)

## 문제 정보
# **문제 이름**: 자릿수 더하기
# **문제 번호**: 120906
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120906)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

## 코드
def solution(n):
    return sum([int(s) for s in str(n)])
