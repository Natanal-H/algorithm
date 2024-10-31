# ------------------------------------------------------
# 문제 번호 : [2738] 행렬 덧셈
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2738
# 난이도 : X
# 분류 : 수학, 구현, 사칙연산
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 코드
N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(2):
    for i in range(N):
        data = list(map(int,input().split()))
        
        for j in range(M):
            arr[i][j] += data[j]
            
for i in range(N):
    print(' '.join(map(str,arr[i])))
