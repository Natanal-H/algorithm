# 프로그래머스 문제 풀이 - 문자열 정렬하기 (2) (120911)

## 문제 정보
# **문제 이름**: 문자열 정렬하기 (2)
# **문제 번호**: 120911
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120911)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
