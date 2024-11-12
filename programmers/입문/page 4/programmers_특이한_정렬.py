# 프로그래머스 문제 풀이 - 특이한 정렬 (120880)

## 문제 정보
# **문제 이름**: 특이한 정렬
# **문제 번호**: 120880
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120880)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))
