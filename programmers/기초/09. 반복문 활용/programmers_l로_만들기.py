# 프로그래머스 문제 풀이 - l로 만들기 (181834)

## 문제 정보
# **문제 이름**: l로 만들기
# **문제 번호**: 181834
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181834)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(myString):
    return ''.join(['l' if s < 'l' else s for s in myString])
