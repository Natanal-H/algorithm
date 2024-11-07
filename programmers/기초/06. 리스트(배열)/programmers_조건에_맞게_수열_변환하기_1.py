# 프로그래머스 문제 풀이 - 조건에 맞게 수열 변환하기 1 (181882)

## 문제 정보
# **문제 이름**: 조건에 맞게 수열 변환하기 1
# **문제 번호**: 181882
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181882)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 
# 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr):
    for i, v in enumerate(arr) :
        if v >= 50 and v % 2 == 0:
            arr[i] //= 2
        elif v < 50 and v % 2:
            arr[i] *= 2
    return arr
