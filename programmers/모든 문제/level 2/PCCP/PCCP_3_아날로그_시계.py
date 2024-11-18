# 프로그래머스 문제 풀이 - [PCCP 기출문제] 3번 / 아날로그 시계 (250135)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 3번 / 아날로그 시계
# **문제 번호**: 250135
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/250135)
# **풀이 날짜** : 2024-11-18

## 문제 
# 문제 설명 :
# 시침, 분침, 초침이 있는 아날로그시계가 있습니다. 시계의 시침은 12시간마다, 분침은 60분마다, 초침은 60초마다 시계를 한 바퀴 돕니다. 
# 따라서 시침, 분침, 초침이 움직이는 속도는 일정하며 각각 다릅니다. 이 시계에는 초침이 시침/분침과 겹칠 때마다 알람이 울리는 기능이 있습니다. 
# 당신은 특정 시간 동안 알람이 울린 횟수를 알고 싶습니다.

## 코드
def getCount(h, m, s) :
    sd = s * 6
    md = m * 6 + s * 0.1
    hd = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360
    
    ret = (h * 60 + m) * 2 - h
    if h >= 12 : ret -= 2
    if sd >= md : ret += 1
    if sd >= hd : ret += 1
    
    return ret
    
def solution(h1, m1, s1, h2, m2, s2):
    answer = getCount(h2, m2, s2) - getCount(h1, m1, s1)   
    if h1 in [0, 12] and m1 == 0 and s1 == 0:
        answer += 1
    return answer
