# 프로그래머스 문제 풀이 - 이진수 더하기 (120885)

## 문제 정보
# **문제 이름**: 이진수 더하기
# **문제 번호**: 120885
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120885)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(bin1, bin2):
    return str(bin(int(bin1, 2) + int(bin2, 2)))[2:]
