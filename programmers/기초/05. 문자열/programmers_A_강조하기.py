# 프로그래머스 문제 풀이 - A 강조하기 (181874)

## 문제 정보
# **문제 이름**: A 강조하기
# **문제 번호**: 181874
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181874)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, 
# "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

## 코드
def solution(myString):
    return myString.lower().replace('a','A')
