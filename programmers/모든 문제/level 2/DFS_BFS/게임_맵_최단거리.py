# 프로그래머스 문제 풀이 - 게임 맵 최단거리 (1844)

## 문제 정보
# **문제 이름**: 게임 맵 최단거리
# **문제 번호**: 1844
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/1844)
# **풀이 날짜** : 2024-11-19

## 문제 
# 문제 설명 :
# ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.
# 게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 
# 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요. 
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

## 코드
from collections import deque

def solution(maps):
    r, c = len(maps), len(maps[0])
    arr = [[0 for _ in range(c)] for _ in range(r)]
    q = deque();    q.append((1, 0, 0))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        n, x, y = q.popleft()
        if x == r-1 and y == c-1 : return n
        if not (arr[x][y] == 0 or arr[x][y] > n) : continue
        
        arr[x][y] = n
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1 :
                q.append((n+1, nx, ny))
                
    return -1
