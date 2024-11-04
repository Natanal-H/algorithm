# ------------------------------------------------------
# 문제 번호 : [11651] 좌표 정렬하기 2
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/11651
# 난이도 : X
# 분류 : 정렬
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 코드
import sys

N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr.append([y, x])

arr.sort()
                                               
for a in arr :
    print(f"{a[1]} {a[0]}")
