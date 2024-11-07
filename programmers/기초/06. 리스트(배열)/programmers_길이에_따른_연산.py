# 프로그래머스 문제 풀이 - 길이에 따른 연산 (181882)

## 문제 정보
# **문제 이름**: 길이에 따른 연산
# **문제 번호**: 181882
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181882)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수가 담긴 리스트 num_list가 주어질 때, 
# 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list):
    a = 1
    
    if len(num_list) <= 10 :
        for n in num_list :
            a *= n
    else :
        a = sum(num_list)
    
    return a
