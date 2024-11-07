# 프로그래머스 문제 풀이 - ad 제거하기 (181870)

## 문제 정보
# **문제 이름**: ad 제거하기
# **문제 번호**: 181870
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181870)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고
# 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(strArr):
    answer = []
    
    for s in strArr :
        if not "ad" in s :
            answer.append(s)
    
    return answer
