# 프로그래머스 문제 풀이 - 잘라서 배열로 저장하기 (120913)

## 문제 정보
# **문제 이름**: 잘라서 배열로 저장하기
# **문제 번호**: 120913
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120913)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]
