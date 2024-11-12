# 프로그래머스 문제 풀이 - A로 B 만들기 (120886)

## 문제 정보
# **문제 이름**: A로 B 만들기
# **문제 번호**: 120886
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120886)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(before, after):
    return int(sorted(before) == sorted(after))
