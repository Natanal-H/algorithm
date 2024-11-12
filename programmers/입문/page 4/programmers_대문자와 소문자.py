# 프로그래머스 문제 풀이 - 대문자와 소문자 (120893)

## 문제 정보
# **문제 이름**: 대문자와 소문자
# **문제 번호**: 120893
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120893)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_string):
    return ''.join([s.upper() if 'a'<= s <= 'z' else s.lower() for s in my_string])

## 다른 코드
def solution(my_string):
    return my_string.swapcase()
