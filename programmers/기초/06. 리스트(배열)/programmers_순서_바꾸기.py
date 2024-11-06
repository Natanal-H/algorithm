# 프로그래머스 문제 풀이 - 순서 바꾸기 (181891)

## 문제 정보
# **문제 이름**: 순서 바꾸기
# **문제 번호**: 181891
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181891)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 리스트 num_list와 정수 n이 주어질 때, 
# num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 
# n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list, n):
    return num_list[n:] + num_list[:n]
