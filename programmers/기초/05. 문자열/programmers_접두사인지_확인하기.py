# 프로그래머스 문제 풀이 - 접두사인지 확인하기 (181906)

## 문제 정보
# **문제 이름**: 접두사인지 확인하기
# **문제 번호**: 181906
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181906)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 
# 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, is_prefix):
    return int(my_string[:len(is_prefix)] == is_prefix)
