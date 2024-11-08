# 프로그래머스 문제 풀이 - 최댓값 만들기 (2) (120862)

## 문제 정보
# **문제 이름**: 최댓값 만들기 (2)
# **문제 번호**: 120862
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120862)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(numbers):
    numbers.sort()
    return max(numbers[-1]*numbers[-2], numbers[0]*numbers[1])
