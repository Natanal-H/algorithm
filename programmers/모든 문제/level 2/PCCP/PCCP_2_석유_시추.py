# 프로그래머스 문제 풀이 - [PCCP 기출문제] 2번 / 석유 시추 (250136)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 2번 / 석유 시추
# **문제 번호**: 250136
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/250136)
# **풀이 날짜** : 2024-11-18

## 문제 
# 문제 설명 :
# 세로길이가 n 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 
# 당신이 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 
# 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.
#
# 석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 land가 매개변수로 주어집니다. 
# 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.

## 코드
from collections import deque

def solution(land):
    answer = 0
    index = 1
    r, c = len(land), len(land[0])
    visited = [[False] * c for _ in range(r)]
    dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
    oils, arr = {}, []
    
    def bfs(x, y):
        q, n = deque([[x, y]]), 1
        visited[x][y] = True
        land[x][y] = index

        while q:
            qx, qy = q.popleft()

            for i in range(4):
                X, Y = qx + dx[i], qy + dy[i]

                if 0 <= X < r and 0 <= Y < c and visited[X][Y] == False and land[X][Y] != 0:
                    n += 1
                    visited[X][Y] = True
                    land[X][Y] = index
                    q.append([X, Y])

        oils[index] = n
    
    for i in range(r):
        for j in range(c):
            if land[i][j] and not visited[i][j] :
                bfs(i, j)
                index += 1
    
    for j in range(c):
        s = set()
        total = 0
        for i in range(r):
            if land[i][j] != 0:
                s.add(land[i][j])
        for a in s:
            total += oils[a]
        arr.append(total)
    
    return max(arr)
