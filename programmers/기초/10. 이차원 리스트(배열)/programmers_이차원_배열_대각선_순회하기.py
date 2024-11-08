# 프로그래머스 문제 풀이 - 이차원 배열 대각선 순회하기 (181829)

## 문제 정보
# **문제 이름**: 이차원 배열 대각선 순회하기
# **문제 번호**: 181829
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181829)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 2차원 정수 배열 board와 정수 k가 주어집니다.
# i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(board, k):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j > k:
                break
            answer += board[i][j]
    
    return answer
