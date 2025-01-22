# 프로그래머스 문제 풀이 - 리코쳇 로봇 (169199)

## 문제 정보
# **문제 이름**: 리코쳇 로봇
# **문제 번호**: 169199
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/169199)
# **풀이 날짜** : 2025-01-22

## 문제 
# 문제 설명 :
# 리코쳇 로봇이라는 보드게임이 있습니다.
# 이 보드게임은 격자모양 게임판 위에서 말을 움직이는 게임으로, 시작 위치에서 출발한 뒤 목표 위치에 정확하게 멈추기 위해 최소 몇 번의 이동이 필요한지 말하는 게임입니다.
# 이 게임에서 말의 이동은 현재 위치에서 상, 하, 좌, 우 중 한 방향으로 게임판 위의 장애물이나 게임판 가장자리까지 부딪힐 때까지 미끄러져 움직이는 것을 한 번의 이동으로 정의합니다.
# 게임판의 상태를 나타내는 문자열 배열 board가 주어졌을 때, 말이 목표위치에 도달하는데 최소 몇 번 이동해야 하는지 return 하는 solution함수를 완성해주세요. 
# 만약 목표위치에 도달할 수 없다면 -1을 return 해주세요.

## 코드
from collections import deque

def findChar(board, char):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == char : return i, j

def solution(board):
    board = [[char for char in string] for string in board]
    visited = [[False for _ in b] for b in board]
    gx, gy = findChar(board, 'G')
    rx, ry = findChar(board, 'R')    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((rx, ry, 0))
    
    def go(x, y, i):
        a, b = x, y
        while True:
            xx, yy = a + dx[i], b + dy[i]
            if xx < 0 or xx >= len(board) or yy < 0 or yy >= len(board[0]) or board[xx][yy] == 'D' :
                break
            else :
                a, b = xx, yy
        return a, b
        
    while q :
        x, y, n = q.popleft()
        if x == gx and y == gy: return n
        if visited[x][y] : continue
        visited[x][y] = True
        
        for i in range(4):
            xx, yy = go(x, y, i)
            if not visited[xx][yy] : q.append((xx, yy, n+1))
    
    return -1
