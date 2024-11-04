# ------------------------------------------------------
# 문제 번호 : [1018] 체스판 다시 칠하기 
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1018
# 난이도 : X
# 분류 : 브루트 포스 알고리즘
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 브루트 포스(Brute Force) 알고리즘은 문제를 해결하기 위해 가능한 모든 경우의 수를 탐색하는 방법입니다.

# 문제 설명 :
# MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
# 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
#
# 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 코드
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

ans = 64
B = ['WBWBWBWB', 'BWBWBWBW']

def check_board(y, x, z):
    cnt = 0
    for a in range(8):
        for b in range(8):
            if arr[y+a][x+b] != B[(a+z)%2][b]:
                cnt+=1
            if cnt >= ans :
                return 64
    return cnt
    
for n in range(N-7):
    for m in range(M-7):
        ans = min(ans, check_board(n,m,0), check_board(n,m,1))
        
print(ans)
