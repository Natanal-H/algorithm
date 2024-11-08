# 프로그래머스 문제 풀이 - 숨어있는 숫자의 덧셈 (2) (120864)

## 문제 정보
# **문제 이름**: 숨어있는 숫자의 덧셈 (2)
# **문제 번호**: 120864
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120864)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_string):
    nums = ''.join([' ' if s.isalpha() else s for s in my_string]).split()    
    return sum([int(n) for n in nums])
