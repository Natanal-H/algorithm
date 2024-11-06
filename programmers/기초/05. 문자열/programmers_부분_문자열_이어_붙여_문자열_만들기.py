# 프로그래머스 문제 풀이 - 부분 문자열 이어 붙여 문자열 만들기 (181911)

## 문제 정보
# **문제 이름**: 부분 문자열 이어 붙여 문자열 만들기
# **문제 번호**: 181911
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181911)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. 
# parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 
# 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_strings, parts):
    return ''.join([my_strings[i][v[0]:v[1]+1] for i,v in enumerate(parts)])
