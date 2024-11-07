# 프로그래머스 문제 풀이 - 정수 찾기 (181840)

## 문제 정보
# **문제 이름**: 정수 찾기
# **문제 번호**: 181840
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181840)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list, n):
    return int(n in num_list)
