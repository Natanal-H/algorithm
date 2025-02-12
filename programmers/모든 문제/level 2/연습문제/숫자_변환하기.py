# 프로그래머스 문제 풀이 - 숫자 변환하기 (154538)

## 문제 정보
# **문제 이름**: 숫자 변환하기
# **문제 번호**: 154538
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/154538)
# **풀이 날짜** : 2025-01-20

## 문제 
# 문제 설명 :
# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.
# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.
# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

## 코드
from collections import deque

def solution(x, y, n):
    q = deque()
    q.append((y, 0))
    
    while q :
        i, j = q.popleft()
        if i == x : return j
    
        k = i - n
        if k >= x :
            q.append((k, j + 1))
        
        k = i / 2
        if k % 1 == 0 and k >= x :
            q.append((k, j + 1))
        
        k = i / 3
        if k % 1 == 0 and k >= x :
            q.append((k, j + 1))
    
    return -1
