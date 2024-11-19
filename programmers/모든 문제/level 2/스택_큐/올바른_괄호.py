# 프로그래머스 문제 풀이 - 올바른 괄호 (12909)

## 문제 정보
# **문제 이름**: 올바른 괄호
# **문제 번호**: 12909
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12909)
# **풀이 날짜** : 2024-11-19

## 문제 
# 문제 설명 :
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(s):  
    cnt = 0
    for i in s:
        if cnt < 0: return False
        
        if i == '(':    cnt += 1
        else:           cnt -= 1

    if cnt != 0:    return False
    return True
