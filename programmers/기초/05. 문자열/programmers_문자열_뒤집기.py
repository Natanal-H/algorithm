# 프로그래머스 문제 풀이 - 문자열 뒤집기 (181905)

## 문제 정보
# **문제 이름**: 문자열 뒤집기
# **문제 번호**: 181905
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181905)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
