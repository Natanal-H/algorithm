# 프로그래머스 문제 풀이 - n보다 커질 때까지 더하기 (181884)

## 문제 정보
# **문제 이름**: n보다 커질 때까지 더하기
# **문제 번호**: 181884
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181884)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. 
# numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(numbers, n):
    answer = 0
    for num in numbers :
        answer += num
        if answer > n : break
    return answer
