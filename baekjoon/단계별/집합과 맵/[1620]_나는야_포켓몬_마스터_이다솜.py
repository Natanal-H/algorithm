# ------------------------------------------------------
# 문제 번호 : [1620] 나는야 포켓몬 마스터 이다솜
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1620
# 난이도 : X
# 분류 : 자료 구조, 해시를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.
# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와.
# 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해.

# 코드
import sys

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
    inp = sys.stdin.readline().strip()
    
    dic[str(i)] = inp
    dic[inp] = str(i)
        
L = []

for _ in range(M):
    L.append(dic[sys.stdin.readline().strip()])
    
[print(l) for l in L]
