# 프로그래머스 문제 풀이 - 부분 문자열 (181842)

## 문제 정보
# **문제 이름**: 부분 문자열
# **문제 번호**: 181842
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181842)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
# 문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(str1, str2):
    return int(str1 in str2)
