# 프로그래머스 문제 풀이 - [PCCP 기출문제] 9번 / 지폐 접기 (340199)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 9번 / 지폐 접기
# **문제 번호**: 340199
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340199)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 민수는 다양한 지폐를 수집하는 취미를 가지고 있습니다. 지폐마다 크기가 달라 지갑에 넣으려면 여러 번 접어서 넣어야 합니다.
# 지폐를 접을 때는 다음과 같은 규칙을 지킵니다.
# 지폐를 접을 때는 항상 길이가 긴 쪽을 반으로 접습니다.
# 접기 전 길이가 홀수였다면 접은 후 소수점 이하는 버립니다.
# 접힌 지폐를 그대로 또는 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
#
# 지갑의 가로, 세로 크기를 담은 정수 리스트 wallet과 지폐의 가로, 세로 크기를 담은 정수 리스트 bill가 주어질 때,
# 지갑에 넣기 위해서 지폐를 최소 몇 번 접어야 하는지 return하도록 solution함수를 완성해 주세요.

## 코드
def swap(arg):
    if arg[0] < arg[1]:
        arg[0], arg[1] = arg[1], arg[0]
    return arg

def solution(wallet, bill):
    answer = 0
    wallet, bill = swap(wallet), swap(bill)
    
    while wallet[0]<bill[0] or wallet[1]<bill[1] :
        answer += 1
        bill[0] //= 2
        bill = swap(bill)
    
    return answer
