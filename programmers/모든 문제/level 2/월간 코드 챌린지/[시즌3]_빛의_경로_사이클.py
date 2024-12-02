# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌3] 빛의 경로 사이클 (86052)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌3] 빛의 경로 사이클
# **문제 번호**: 86052
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/86052)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 각 칸마다 S, L, 또는 R가 써져 있는 격자가 있습니다. 당신은 이 격자에서 빛을 쏘고자 합니다. 이 격자의 각 칸에는 다음과 같은 특이한 성질이 있습니다.
# 빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
# 빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
# 빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
# 빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
# 당신은 이 격자 내에서 빛이 이동할 수 있는 경로 사이클이 몇 개 있고, 각 사이클의 길이가 얼마인지 알고 싶습니다. 경로 사이클이란, 빛이 이동하는 순환 경로를 의미합니다.
#
# 격자의 정보를 나타내는 1차원 문자열 배열 grid가 매개변수로 주어집니다. 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(grid):
    answer = []
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    lx, ly = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(ly)] for _ in range(lx)]
    
    for x in range(lx):
        for y in range(ly):
            for i in range(4):
                if visited[x][y][i] : continue
                cnt = 0
                nx, ny = x, y
                while not visited[nx][ny][i]:
                    visited[nx][ny][i] = True
                    cnt += 1
                    if grid[nx][ny] == "S": pass
                    elif grid[nx][ny] == "L": i = (i + 3) % 4
                    elif grid[nx][ny] == "R": i = (i + 1) % 4
                    ny = (ny + dy[i]) % ly
                    nx = (nx + dx[i]) % lx
                answer.append(cnt)    
    return sorted(answer)
