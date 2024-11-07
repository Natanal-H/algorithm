# 프로그래머스 문제 풀이 - 공백으로 구분하기 2 (181868)

## 문제 정보
# **문제 이름**: 공백으로 구분하기 2
# **문제 번호**: 181868
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181868)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
# my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string):
    return list(my_string.split())
