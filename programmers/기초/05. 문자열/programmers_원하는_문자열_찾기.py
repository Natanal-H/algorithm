# 프로그래머스 문제 풀이 - 원하는 문자열 찾기 (181878)

## 문제 정보
# **문제 이름**: 원하는 문자열 찾기
# **문제 번호**: 181878
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181878)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. 
# myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
# 단, 알파벳 대문자와 소문자는 구분하지 않습니다.

## 코드
def solution(myString, pat):
    return int(pat.lower() in myString.lower())
