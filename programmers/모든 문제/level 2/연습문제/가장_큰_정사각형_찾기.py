# 프로그래머스 문제 풀이 - 가장 큰 정사각형 찾기 (12905)

## 문제 정보
# **문제 이름**: 가장 큰 정사각형 찾기
# **문제 번호**: 12905
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12905)
# **풀이 날짜** : 2024-11-19

## 문제 
# 문제 설명 :
# 1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요.
# (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

## 코드
def solution(board):
    answer = max(board[0])
    
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])

    return answer ** 2
