# 프로그래머스 문제 풀이 - 문자열의 앞의 n글자 (181907)

## 문제 정보
# **문제 이름**: 문자열의 앞의 n글자
# **문제 번호**: 181907
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181907)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, n):
    return my_string[:n]
