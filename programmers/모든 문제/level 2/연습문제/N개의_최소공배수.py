# 프로그래머스 문제 풀이 - N개의 최소공배수 (12953)

## 문제 정보
# **문제 이름**: N개의 최소공배수
# **문제 번호**: 12953
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12953)
# **풀이 날짜** : 2024-11-21

## 문제 
# 문제 설명 :
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

## 코드
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def solution(arr):
    answer = 1
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer
