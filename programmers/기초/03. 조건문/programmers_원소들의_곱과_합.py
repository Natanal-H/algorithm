# 프로그래머스 문제 풀이 - 원소들의 곱과 합 (181929)

## 문제 정보
# **문제 이름**: 원소들의 곱과 합
# **문제 번호**: 181929
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181929)

## 문제 
# 문제 설명 :
# 정수가 담긴 리스트 num_list가 주어질 때, 
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list):
    s = 0; m = 1
    for n in num_list:
        s += n; m *= n
    return int(m < s**2)
