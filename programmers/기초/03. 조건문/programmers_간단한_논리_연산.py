# 프로그래머스 문제 풀이 - 간단한 논리 연산 (181917)

## 문제 정보
# **문제 이름**: 간단한 논리 연산
# **문제 번호**: 181917
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181917)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.
# (x1 ∨ x2) ∧ (x3 ∨ x4)
#
# x	y	x∨y	x∧y
# T	T  T     T
# T	F	 T	   F
# F	T	 T     F
# F	F	 F     F

# 문제 풀이 :
# 진리표에 따르면 ∨ => or	∧ => and 논리 연산자

## 코드
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)
