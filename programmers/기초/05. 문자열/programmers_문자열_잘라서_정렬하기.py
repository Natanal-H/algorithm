# 프로그래머스 문제 풀이 - 문자열 잘라서 정렬하기 (181866)

## 문제 정보
# **문제 이름**: 문자열 잘라서 정렬하기
# **문제 번호**: 181866
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181866)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, 빈 문자열은 반환할 배열에 넣지 않습니다.

## 코드
def solution(myString):
    return sorted(list(myString.replace('x', ' ').split()))
