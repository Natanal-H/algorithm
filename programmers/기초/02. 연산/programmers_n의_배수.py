# 프로그래머스 문제 풀이 - n의 배수 (181937)

## 문제 정보
# **문제 이름**: n의 배수
# **문제 번호**: 181937
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181937)

## 문제 
# 문제 설명 :
# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return 
# n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num, n):
    return 1 if num % n == 0 else 0
