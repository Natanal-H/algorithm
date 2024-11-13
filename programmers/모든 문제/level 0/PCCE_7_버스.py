# 프로그래머스 문제 풀이 - [PCCE 기출문제] 7번 / 버스 (340201)

## 문제 정보
# **문제 이름**: [PCCE 기출문제] 7번 / 버스
# **문제 번호**: 340201
# **문제 레벨**: 0
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340201)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 버스에는 좌석이 총 seat개만큼 있습니다. 영진이는 버스 좌석에 앉아서 갈 수 있을지 궁금해합니다. 
# 기점에서 출발한 버스가 영진이가 기다리는 정거장에 도착하기 전에 방문하는 각 정거장에서 승/하차한 승객 정보가 주어질 때, 영진이가 버스에 탄 순간 빈 좌석은 몇 개인지 구해주세요.

## 코드
def func1(num):
    if 0 > num:
        return 0
    else:
        return num

def func2(num):
    if num > 0:
        return 0
    else:
        return num

def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num
    
def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num

    
def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)
        num_passenger -= func3(station)
    answer = func1(seat - num_passenger)
    return answer
