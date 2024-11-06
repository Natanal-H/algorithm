# 프로그래머스 문제 풀이 - 접미사 배열 (181909)

## 문제 정보
# **문제 이름**: 접미사 배열
# **문제 번호**: 181909
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181909)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])
