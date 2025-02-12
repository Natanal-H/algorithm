# 프로그래머스 문제 풀이 - 특정 문자 제거하기 (120826)

## 문제 정보
# **문제 이름**: 특정 문자 제거하기
# **문제 번호**: 120826
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120826)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_string, letter):
    return my_string.replace(letter, '')
