# 프로그래머스 문제 풀이 - 문자 반복 출력하기 (120825)

## 문제 정보
# **문제 이름**: 문자 반복 출력하기
# **문제 번호**: 120825
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120825)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(my_string, n):
    return ''.join([s*n for s in my_string])
