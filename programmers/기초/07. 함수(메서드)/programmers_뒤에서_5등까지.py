# 프로그래머스 문제 풀이 - 뒤에서 5등까지 (181853)

## 문제 정보
# **문제 이름**: 뒤에서 5등까지
# **문제 번호**: 181853
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181853)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list):
    return sorted(num_list)[:5]
