# 프로그래머스 문제 풀이 - 배열 만들기 1 (181901)

## 문제 정보
# **문제 이름**: 배열 만들기 1
# **문제 번호**: 181901
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181901)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(n, k):
    return list(range(k,n+1,k))
