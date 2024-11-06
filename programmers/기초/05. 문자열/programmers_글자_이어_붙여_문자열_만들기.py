# 프로그래머스 문제 풀이 - 글자 이어 붙여 문자열 만들기 (181915)

## 문제 정보
# **문제 이름**: 글자 이어 붙여 문자열 만들기
# **문제 번호**: 181915
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181915)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])
