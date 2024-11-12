# 프로그래머스 문제 풀이 - 가장 큰 수 찾기 (120899)

## 문제 정보
# **문제 이름**: 가장 큰 수 찾기
# **문제 번호**: 120899
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120899)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(array):
    return [max(array), array.index(max(array))]
