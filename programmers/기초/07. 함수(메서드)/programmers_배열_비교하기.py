# 프로그래머스 문제 풀이 - 배열 비교하기 (181856)

## 문제 정보
# **문제 이름**: 배열 비교하기
# **문제 번호**: 181856
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181856)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
# 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
#
# 두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 
# 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.

## 코드
def compare(a, b):
    if len(a) != len(b) :
        return 1 if len(a) > len(b) else -1
    
    return 1 if sum(a) > sum(b) else (-1 if sum(a) < sum(b) else 0)

def solution(arr1, arr2):
    return compare(arr1, arr2)
