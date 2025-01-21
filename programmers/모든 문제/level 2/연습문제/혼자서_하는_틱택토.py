# 프로그래머스 문제 풀이 - 혼자서 하는 틱택토 (160585)

## 문제 정보
# **문제 이름**: 혼자서 하는 틱택토
# **문제 번호**: 160585
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/160585)
# **풀이 날짜** : 2025-01-21

## 문제 
# 문제 설명 :
# 틱택토는 두 사람이 하는 게임으로 처음에 3x3의 빈칸으로 이루어진 게임판에 선공이 "O", 후공이 "X"를 번갈아가면서 빈칸에 표시하는 게임입니다. 
# 가로, 세로, 대각선으로 3개가 같은 표시가 만들어지면 같은 표시를 만든 사람이 승리하고 게임이 종료되며 9칸이 모두 차서 더 이상 표시를 할 수 없는 경우에는 무승부로 게임이 종료됩니다.
#
# 머쓱이가 혼자서 게임을 진행하다 의문이 생긴 틱택토 게임판의 정보를 담고 있는 문자열 배열 board가 매개변수로 주어질 때, 
# 이 게임판이 규칙을 지켜서 틱택토를 진행했을 때 나올 수 있는 게임 상황이면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

## 코드
def count(b, c):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == c: cnt += 1 
    return cnt

def check(b, c):
    for s in b :
        if ''.join(s) == c * 3: return True
    
    b = list(map(list, zip(*b)))
    
    for s in b :
        if ''.join(s) == c * 3: return True
    
    if b[0][0] == b[1][1] == b[2][2] and b[1][1] == c: return True
    if b[0][2] == b[1][1] == b[2][0] and b[1][1] == c: return True
    
    return False

def solution(board):
    board = [[char for char in string] for string in board]
    
    cnt_o, cnt_x = count(board, 'O'), count(board, 'X')
    
    if cnt_o == 0 and cnt_x == 0 : return 1
    if cnt_o - cnt_x < 0 or cnt_o - cnt_x > 1 : return 0 
    
    chk_o, chk_x = check(board, 'O'), check(board, 'X')

    if chk_x and (chk_o or cnt_o - cnt_x == 1) : return 0
    if chk_o and cnt_o - cnt_x == 0 : return 0 
    
    return 1
