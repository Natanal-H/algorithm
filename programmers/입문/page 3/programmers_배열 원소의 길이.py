# 프로그래머스 문제 풀이 - 배열 원소의 길이 (120854)

## 문제 정보
# **문제 이름**: 배열 원소의 길이
# **문제 번호**: 120854
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120854)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(strlist):
    return [len(s) for s in strlist]
