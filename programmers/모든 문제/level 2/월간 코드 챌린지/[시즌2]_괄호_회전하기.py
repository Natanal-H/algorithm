# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌2] 괄호 회전하기 (76502)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌2] 괄호 회전하기
# **문제 번호**: 76502
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/76502)
# **풀이 날짜** : 2024-11-29

## 문제 
# 문제 설명 :
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다. (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

## 코드
from collections import deque

def is_right(q):
    d = {')':'(', '}':'{', ']':'['}
    s = []
    
    while q:
        a = q.popleft()
        if a in d.values() : s.append(a)
        else :
            if len(s) == 0 : return 0
            elif s[-1] == d[a] : s.pop()
            else : return 0
    
    return 1

def solution(s):
    if len(s) % 2 : return 0
    
    answer = 0
    dq = deque(s)
    
    for _ in range(len(s)):
        answer += is_right(deque(dq))
        dq.rotate(-1)
        
    return answer
