# 프로그래머스 문제 풀이 - 홀수 vs 짝수 (181887)

## 문제 정보
# **문제 이름**: 홀수 vs 짝수
# **문제 번호**: 181887
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181887)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 
# 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

## 코드
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))
