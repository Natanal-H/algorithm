# 프로그래머스 문제 풀이 - 짝수 홀수 개수 (120824)

## 문제 정보
# **문제 이름**: 짝수 홀수 개수
# **문제 번호**: 120824
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120824)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(num_list):
    answer = [0, 0]
    
    for num in num_list:
        answer[num%2] += 1
    
    return answer
