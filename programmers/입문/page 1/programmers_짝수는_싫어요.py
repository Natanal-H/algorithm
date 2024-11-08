# 프로그래머스 문제 풀이 - 짝수는 싫어요 (120813)

## 문제 정보
# **문제 이름**: 짝수는 싫어요
# **문제 번호**: 120813
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120813)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):  
    return [i for i in range(1,n+1,2)]
