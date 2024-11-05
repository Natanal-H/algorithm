# ------------------------------------------------------
# 문제 번호 : [14425] 문자열 집합
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/14425
# 난이도 : X
# 분류 : 자료 구조, 문자열, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 총 N개의 문자열로 이루어진 집합 S가 주어진다.
# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

# 코드
import sys

N, M = map(int, input().split())
S = set()
SM = set()

for _ in range(N):
    S.add(sys.stdin.readline().strip())
    
for _ in range(M):
    SM.add(sys.stdin.readline().strip())

if len(S & SM) == 0: print(0)
else :
    print(M - (len(S | SM) - N))

