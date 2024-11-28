# 프로그래머스 문제 풀이 - [Summer/Winter Coding(~2018)] 방문 길이 (49994)

## 문제 정보
# **문제 이름**: [Summer/Winter Coding(~2018)] 방문 길이
# **문제 번호**: 49994
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/49994)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
# U: 위쪽으로 한 칸 가기
# D: 아래쪽으로 한 칸 가기
# R: 오른쪽으로 한 칸 가기
# L: 왼쪽으로 한 칸 가기
# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다.
# 명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(dirs):
    answer = 0
    dic = {'L':0, 'R':1, 'U':2, 'D':3 }
    dy, dx = [0,0,1,-1], [-1,1,0,0]
    check = [[[True for _ in range(2)]
             for _ in range(11)] for _ in range(11)]
    x, y = 5, 5
    
    for d in dirs:
        i = dic[d]
        
        if not (0 <= x + dx[i] <= 10 and 0 <= y + dy[i] <= 10) : continue
        
        if i % 2 :
            answer += int(check[y][x][i//2])
            check[y][x][i//2] = False
        else :
            answer += int(check[y+dy[i]][x+dx[i]][i//2])
            check[y+dy[i]][x+dx[i]][i//2] = False
 
        x += dx[i]; y += dy[i] 
    
    return answer
