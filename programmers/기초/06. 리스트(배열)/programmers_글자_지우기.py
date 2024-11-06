# 프로그래머스 문제 풀이 - 글자 지우기 (181900)

## 문제 정보
# **문제 이름**: 글자 지우기
# **문제 번호**: 181900
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181900)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 배열 indices가 주어질 때, 
# my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, indices):
    indices.sort(reverse=True)
    
    for i in indices:
        my_string = my_string[:i] + my_string[i+1:]
    
    return my_string
