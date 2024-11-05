# 프로그래머스 문제 풀이 - 마지막 두 원소 (181927)

## 문제 정보
# **문제 이름**: 마지막 두 원소
# **문제 번호**: 181927
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181927)
# **풀이 날짜** : 2024-11-05

## 문제 
# 문제 설명 :
# 정수 리스트 num_list가 주어질 때, 
# 마지막 원소가 그 전 원소보다 크면 마지막 원소에서 그 전 원소를 뺀 값을
# 마지막 원소가 그 전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list):
    last = num_list[len(num_list) - 1]
    last2 = num_list[len(num_list) - 2]
    
    if last > last2 : 
        num_list.append(last - last2)
    else :
        num_list.append(last * 2)
        
    return num_list
