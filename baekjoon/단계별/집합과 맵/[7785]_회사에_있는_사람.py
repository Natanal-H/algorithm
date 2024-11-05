# ------------------------------------------------------
# 문제 번호 : [7785] 회사에 있는 사람
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/7785
# 난이도 : X
# 분류 : 자료 구조, 해시를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 
# 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

# 코드
import sys

N = int(input())
S = set()

for _ in range(N):
    inp = sys.stdin.readline().strip().split()
    
    if inp[1] == 'enter' :
        S.add(inp[0])
    else:
        S.remove(inp[0])
        
S = sorted(list(S), reverse=True)
[print(name) for name in S]
