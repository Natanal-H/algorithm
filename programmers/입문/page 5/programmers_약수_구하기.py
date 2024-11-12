# 프로그래머스 문제 풀이 - 약수 구하기 (120897)

## 문제 정보
# **문제 이름**: 약수 구하기
# **문제 번호**: 120897
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120897)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    return [i for i in range(1,n+1) if n % i == 0]
