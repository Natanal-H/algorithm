# 프로그래머스 문제 풀이 - 문자열 정렬하기 (1) (120850)

## 문제 정보
# **문제 이름**: 문자열 정렬하기 (1)
# **문제 번호**: 120850
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120850)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

## 코드
def solution(my_string):
    answer = []
    
    for s in my_string:
        if '0' <= s <= '9' : answer.append(int(s))
    
    return sorted(answer)
