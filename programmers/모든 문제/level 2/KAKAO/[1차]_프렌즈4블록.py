# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [1차] 프렌즈4블록 (17679)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [1차] 프렌즈4블록
# **문제 번호**: 17679
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17679)
# **풀이 날짜** : 2024-11-22

## 문제 
# 문제 설명 :
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
# 만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

## 코드
def solution(m, n, board):
    m, n = n, m
    board = [list(b) for b in zip(*board)]
    
    while True :
        flag = True
        check = [[False for _ in range(n)] for _ in range(m)] 
        
        for i in range(m-1): 
            for j in range(n-1):
                if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] :
                    check[i][j] = check[i+1][j] = check[i][j+1] = check[i+1][j+1] = True
                    flag = False
        
        if flag : break
        
        for i in range(m): 
            for j in range(n):
                if check[i][j] : board[i][j] = ''
            board[i] = ''.join(board[i])
            board[i] = list(' '*(n-len(board[i])) + board[i])
        
    return sum([b.count(' ') for b in board])
