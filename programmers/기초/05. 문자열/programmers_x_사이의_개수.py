# 프로그래머스 문제 풀이 - x 사이의 개수 (181867)

## 문제 정보
# **문제 이름**: x 사이의 개수
# **문제 번호**: 181867
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181867)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때
# 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(myString):
    return [len(s) for s in myString.split('x')]
