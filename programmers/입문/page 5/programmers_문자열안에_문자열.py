# 프로그래머스 문제 풀이 - 문자열안에 문자열 (120908)

## 문제 정보
# **문제 이름**: 문자열안에 문자열
# **문제 번호**: 120908
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120908)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(str1, str2):
    return 1 if str2 in str1 else 2
