# 프로그래머스 문제 풀이 - 배열에서 문자열 대소문자 변환하기 (181875)

## 문제 정보
# **문제 이름**: 배열에서 문자열 대소문자 변환하기
# **문제 번호**: 181875
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181875)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 배열 strArr가 주어집니다. 모든 원소가 알파벳으로만 이루어져 있을 때, 
# 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.

## 코드
def solution(strArr):
    return [s.upper() if i%2 else s.lower() for i, s in enumerate(strArr)]
