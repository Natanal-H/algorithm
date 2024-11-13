# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌2] 약수의 개수와 덧셈 (77884)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌2] 약수의 개수와 덧셈
# **문제 번호**: 77884
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/77884)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(left, right):
    return sum([-n if int(n**0.5) == n**0.5 else n for n in range(left, right+1)])
