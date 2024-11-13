# 프로그래머스 문제 풀이 - 다음에 올 숫자 (120924)

## 문제 정보
# **문제 이름**: 다음에 올 숫자
# **문제 번호**: 120924
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120924)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(common):
    if common[0] * common[2] == common[1] ** 2 :
        if common[0] == 0: 
            return 0
        return int(common[-1] * (common[1] / common[0]))
    else :
        return common[-1] + common[1] - common[0]
