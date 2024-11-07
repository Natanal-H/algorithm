# 프로그래머스 문제 풀이 - 간단한 식 계산하기 (181865)

## 문제 정보
# **문제 이름**: 간단한 식 계산하기
# **문제 번호**: 181865
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181865)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
# 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(binomial):
    answer = 0
    
    binomial = list(binomial.split())
    
    if binomial[1] == '+' : answer = int(binomial[0]) + int(binomial[2])
    if binomial[1] == '-' : answer = int(binomial[0]) - int(binomial[2])
    if binomial[1] == '*' : answer = int(binomial[0]) * int(binomial[2])
    
    return answer
