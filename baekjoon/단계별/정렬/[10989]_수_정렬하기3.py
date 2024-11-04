# ------------------------------------------------------
# 문제 번호 : [10989] 수 정렬하기 3
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10989
# 난이도 : X
# 분류 : 정렬
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 코드
import sys

N = int(input())
cnt = [0] * 10001

for _ in range(N):         
    cnt[int(sys.stdin.readline())] += 1

total = 0
for i in range(10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)
            total += 1
    if total == N :
        break
