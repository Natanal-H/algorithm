# 프로그래머스 문제 풀이 - 세로 읽기 (181904)

## 문제 정보
# **문제 이름**: 세로 읽기
# **문제 번호**: 181904
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181904)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 my_string과 두 정수 m, c가 주어집니다. 
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string, m, c):
    return my_string[c-1::m]
