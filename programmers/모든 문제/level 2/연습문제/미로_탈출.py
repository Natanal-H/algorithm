# 프로그래머스 문제 풀이 - 미로 탈출 (159993)

## 문제 정보
# **문제 이름**: 미로 탈출
# **문제 번호**: 159993
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/159993)
# **풀이 날짜** : 2025-01-21

## 문제 
# 문제 설명 :
# 정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

## 코드
from collections import deque

def init(x, y):
    return [[False for _ in range(y)] for _ in range(x)]

def findChar(maps, char):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == char:
                return i, j

def solution(maps):   
    maps = [[char for char in string] for string in maps]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def find(s, c):
        xs, ys = findChar(maps, s)
        visited = init(len(maps), len(maps[0]))
        
        d = deque()
        d.append((xs, ys, 0))
        
        while d:
            x, y, n = d.popleft()
            
            if maps[x][y] == c : return n
            if visited[x][y]: continue
            visited[x][y] = True
            
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                if xx >= 0 and xx < len(maps) and yy >= 0 and yy < len(maps[xx]) and maps[xx][yy] != 'X' and not visited[xx][yy]:
                    d.append((xx, yy, n+1))
        
        return -1     
    
    StoL, LtoE = find('S', 'L'), find('L', 'E')
    
    if StoL == -1 or LtoE == -1 : return -1
    else : return StoL + LtoE
