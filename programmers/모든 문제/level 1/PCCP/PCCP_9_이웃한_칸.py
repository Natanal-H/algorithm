# 프로그래머스 문제 풀이 - [PCCP 기출문제] 9번 / 이웃한 칸 (250125)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 9번 / 이웃한 칸
# **문제 번호**: 250125
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/250125)
# **풀이 날짜** : 2024-11-18

## 문제 
# 문제 설명 :
# 각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.
# 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.

## 코드
def solution(board, h, w):
    answer = 0
    dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
    
    for k in range(4):
        x, y = h + dx[k], w + dy[k]
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == board[h][w]:
            answer+=1
                       
    return answer
