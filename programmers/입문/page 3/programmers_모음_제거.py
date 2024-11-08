# 프로그래머스 문제 풀이 - 모음 제거 (120849)

## 문제 정보
# **문제 이름**: 모음 제거
# **문제 번호**: 120849
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120849)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_string):
    moem = ['a', 'e', 'i', 'o', 'u']
    for m in moem :
        my_string = my_string.replace(m, '')
    return my_string
