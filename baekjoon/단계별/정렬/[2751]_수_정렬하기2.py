# ------------------------------------------------------
# 문제 번호 : [2751] 수 정렬하기 2
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2751
# 난이도 : X
# 분류 : 정렬
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 코드
import sys

N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
[print(n) for n in arr]
