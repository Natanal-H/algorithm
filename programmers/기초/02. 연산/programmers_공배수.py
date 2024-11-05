# 프로그래머스 문제 풀이 - 공배수 (181936)

## 문제 정보
# **문제 이름**: 공배수
# **문제 번호**: 181936
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181936)

## 문제 
# 문제 설명 :
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을
# 아니라면 0을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(number, n, m):
    return int(number % n == 0 and number % m == 0)
