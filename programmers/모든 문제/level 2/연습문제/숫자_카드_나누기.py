# 프로그래머스 문제 풀이 - 숫자 카드 나누기 (135807)

## 문제 정보
# **문제 이름**: 숫자 카드 나누기
# **문제 번호**: 135807
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/135807)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 철수와 영희는 선생님으로부터 숫자가 하나씩 적힌 카드들을 절반씩 나눠서 가진 후, 다음 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구하려고 합니다.
# 철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고 영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
# 영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고, 철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a
#
# 철수가 가진 카드에 적힌 숫자들을 나타내는 정수 배열 arrayA와 영희가 가진 카드에 적힌 숫자들을 나타내는 정수 배열 arrayB가 주어졌을 때, 주어진 조건을 만족하는 가장 큰 양의 정수 a를 return하도록 solution 함수를 완성해 주세요. 
# 만약, 조건을 만족하는 a가 없다면, 0을 return 해 주세요.

## 코드
from math import gcd

def get_gcd(arr) :
    g = arr[0]
    for i in range(1, len(arr)): g = gcd(g, arr[i])
    return g

def get_divisors(n):
    arr = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  
            arr.append(i)
            if i != n // i:
                arr.append(n // i)
    return sorted(arr, reverse=True)

def get_undividable(arr1, arr2):
    for a in arr1:
        flag = True
        for b in arr2:
            if b % a == 0 : flag = False; break
        if flag : return a
    return 0

def solution(arrayA, arrayB):
    answer = 0
    ga, gb = get_divisors(get_gcd(arrayA)), get_divisors(get_gcd(arrayB))
    
    return max(get_undividable(gb, arrayA), get_undividable(ga, arrayB))

