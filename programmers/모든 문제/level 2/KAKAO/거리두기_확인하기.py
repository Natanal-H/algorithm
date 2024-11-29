# 프로그래머스 문제 풀이 - [2021 카카오 채용연계형 인턴십] 거리두기 확인하기 (81302)

## 문제 정보
# **문제 이름**: [2021 카카오 채용연계형 인턴십] 거리두기 확인하기
# **문제 번호**: 81302
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/81302)
# **풀이 날짜** : 2024-11-29

## 문제 
# 문제 설명 :
# 개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다. 코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
# 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.
# 대기실은 5개이며, 각 대기실은 5x5 크기입니다.
# 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
#
# 5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 
# 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 
# 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## 코드
def check(x, y):
    return 0<=x<5 and 0<=y<5

def inspect(p):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    for x in range(5):
        for y in range(5):
            if p[x][y] != 'P': continue
            for i in range(4):
                if not check(x+dx[i], y+dy[i]) : continue
                xdx, ydy = x+dx[i], y+dy[i]
                if p[xdx][ydy] == 'P' : return 0
                elif p[xdx][ydy] == 'X' : continue
                for j in range(4):
                    if not check(xdx+dx[j], ydy+dy[j]) : continue
                    xdxdx, ydydy = xdx+dx[j], ydy+dy[j]
                    if xdxdx == x and ydydy == y : continue
                    elif p[xdxdx][ydydy] == 'P' : return 0
    return 1

def solution(places):
    answer = [] 
    for place in places : answer.append(inspect(place))
    return answer
