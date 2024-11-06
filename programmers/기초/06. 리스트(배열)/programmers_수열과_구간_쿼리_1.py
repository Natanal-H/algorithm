# 프로그래머스 문제 풀이 - 수열과 구간 쿼리 1 (181883)

## 문제 정보
# **문제 이름**: 수열과 구간 쿼리 1
# **문제 번호**: 181883
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181883)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    return arr
