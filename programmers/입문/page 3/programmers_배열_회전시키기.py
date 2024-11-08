# 프로그래머스 문제 풀이 - 배열 회전시키기 (120844)

## 문제 정보
# **문제 이름**: 배열 회전시키기
# **문제 번호**: 120844
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120844)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction[0] == 'r' else numbers[1:] + [numbers[0]]
