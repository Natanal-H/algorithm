# 프로그래머스 문제 풀이 - 중복된 문자 제거 (120888)

## 문제 정보
# **문제 이름**: 중복된 문자 제거
# **문제 번호**: 120888
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120888)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_string):
    answer = ''
    
    for s in my_string:
        if s not in answer:
            answer += s
    
    return answer

## 다른 코드
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
