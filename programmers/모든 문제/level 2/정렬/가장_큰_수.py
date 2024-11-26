# 프로그래머스 문제 풀이 - 가장 큰 수 (42746)

## 문제 정보
# **문제 이름**: 가장 큰 수
# **문제 번호**: 42746
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42746)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

## 코드
from functools import cmp_to_key

def compare(a, b):
    A, B = int(a+b), int(b+a)
    if A < B:   return 1  
    elif A > B: return -1  
    else:       return 0  

def solution(numbers):    
    return str(int(''.join(sorted(list(map(str, numbers)), key=cmp_to_key(compare)))))
