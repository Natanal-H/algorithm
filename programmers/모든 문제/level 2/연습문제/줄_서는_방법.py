# 프로그래머스 문제 풀이 - 줄 서는 방법 (12936)

## 문제 정보
# **문제 이름**: 줄 서는 방법
# **문제 번호**: 12936
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12936)
# **풀이 날짜** : 2024-11-20

## 문제 
# 문제 설명 :
# n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 
# 사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

## 코드
from math import factorial

def solution(n, k):
    answer = []
    arr = [n for n in range(1,n+1)]
    
    for i in range(n-1,0,-1) :
        f = factorial(i)
        for j in range(len(arr)) :
            if f < k :
                k -= f
            else :
                answer.append(arr.pop(j))
                break
                
    return answer + arr


