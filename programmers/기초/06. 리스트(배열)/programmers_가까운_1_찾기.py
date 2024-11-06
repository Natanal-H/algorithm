# 프로그래머스 문제 풀이 - 가까운 1 찾기 (181898)

## 문제 정보
# **문제 이름**: 가까운 1 찾기
# **문제 번호**: 181898
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181898)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다.
# 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.
# 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

## 코드
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] : return i
    return -1
