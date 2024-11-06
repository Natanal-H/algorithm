# 프로그래머스 문제 풀이 - qr code (181903)

## 문제 정보
# **문제 이름**: qr code
# **문제 번호**: 181903
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181903)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 
# 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(q, r, code):
    return code[r::q]
