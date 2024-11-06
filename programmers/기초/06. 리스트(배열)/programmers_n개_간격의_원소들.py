# 프로그래머스 문제 풀이 - n개 간격의 원소들 (181888)

## 문제 정보
# **문제 이름**: n개 간격의 원소들
# **문제 번호**: 181888
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181888)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 
# 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list, n):
    return num_list[::n]
