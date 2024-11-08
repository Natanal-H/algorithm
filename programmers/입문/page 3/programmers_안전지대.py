# 프로그래머스 문제 풀이 - 안전지대 (120866)

## 문제 정보
# **문제 이름**: 안전지대
# **문제 번호**: 120866
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120866)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(board):
    n = len(board)
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(8) :
                    if not (0 <= i + dy[k] < n) : continue
                    if not (0 <= j + dx[k] < n) : continue
                    if board[i+dy[k]][j+dx[k]] == 0 :
                        board[i+dy[k]][j+dx[k]] = -1
    
    return sum([1 if board[i][j] == 0 else 0 for i in range(n) for j in range(n)])
