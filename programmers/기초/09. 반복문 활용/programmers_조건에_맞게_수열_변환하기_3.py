# 프로그래머스 문제 풀이 - 조건에 맞게 수열 변환하기 3 (181835)

## 문제 정보
# **문제 이름**: 조건에 맞게 수열 변환하기 3
# **문제 번호**: 181835
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181835)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 배열 arr와 자연수 k가 주어집니다.
# 만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k를 더합니다.
# 이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr, k):
    return [a * k if k % 2 else a + k for a in arr]
