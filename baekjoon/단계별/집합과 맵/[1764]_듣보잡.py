# ------------------------------------------------------
# 문제 번호 : [1764] 듣보잡
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1764
# 난이도 : X
# 분류 : 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 코드
import sys

N, M = map(int, input().split())
set_N = set()
set_M = set()

[set_N.add(sys.stdin.readline().strip()) for _ in range(N)]
[set_M.add(sys.stdin.readline().strip()) for _ in range(M)]

L = sorted(list(set_N & set_M))

print(len(L))
[print(name) for name in L]
