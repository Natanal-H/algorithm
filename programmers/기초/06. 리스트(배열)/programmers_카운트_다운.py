# 프로그래머스 문제 풀이 - 카운트 다운 (181899)

## 문제 정보
# **문제 이름**: 카운트 다운
# **문제 번호**: 181899
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181899)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(start_num, end_num):
    return list(range(end_num, start_num + 1))[::-1]
