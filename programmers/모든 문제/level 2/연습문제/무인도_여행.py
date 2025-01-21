# 프로그래머스 문제 풀이 - 무인도 여행 (154540)

## 문제 정보
# **문제 이름**: 무인도 여행
# **문제 번호**: 154540
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/154540)
# **풀이 날짜** : 2025-01-21

## 문제 
# 문제 설명 :
# 메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다. 지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다.
# 지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며, 격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 
# 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다. 이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 
# 지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다. 
# 어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 합니다.
#
# 지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요. 
# 만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.

## 코드
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def solution(maps):
    answer = []
    words = [[char for char in string] for string in maps]
    visited = [[True for _ in range(len(maps[0]))] for _ in range(len(maps))]

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def find(x, y):
        s = int(words[x][y])
        visited[x][y] = False
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if xx >= 0 and yy >= 0 and xx < len(words) and yy < len(words[x]) and words[xx][yy] != 'X' and visited[xx][yy]:
                s += find(xx,yy)
        return s
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] != 'X' and visited[i][j] :
                answer.append(find(i,j))
    
    if len(answer) == 0: answer.append(-1)
    return sorted(answer)
