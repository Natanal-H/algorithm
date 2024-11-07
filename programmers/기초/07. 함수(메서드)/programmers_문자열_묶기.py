# 프로그래머스 문제 풀이 - 문자열 묶기 (181855)

## 문제 정보
# **문제 이름**: 문자열 묶기
# **문제 번호**: 181855
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181855)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 배열 strArr이 주어집니다. strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때
# 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(strArr):
    answer = 0
    dic = {}
    for s in strArr:
        dic[len(s)] = dic.get(len(s), 0) + 1
        answer = max(answer, dic[len(s)])
    return answer
