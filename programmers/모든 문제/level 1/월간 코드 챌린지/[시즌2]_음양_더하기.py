# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌2] 음양 더하기 (76501)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌2] 음양 더하기
# **문제 번호**: 76501
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/76501)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))])
