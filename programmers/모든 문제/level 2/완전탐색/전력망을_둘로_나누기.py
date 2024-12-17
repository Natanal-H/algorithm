# 프로그래머스 문제 풀이 - 전력망을 둘로 나누기 (86971)

## 문제 정보
# **문제 이름**: 전력망을 둘로 나누기
# **문제 번호**: 86971
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/86971)
# **풀이 날짜** : 2024-12-17

## 문제 
# 문제 설명 :
# n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
# 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.
#
# 송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때,
# 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

## 코드
from collections import deque

def solution(n, wires):
    answer = 100
    d = {}
    
    for w in wires:
        for i in range(2):  
            if w[i%2] in d : d[w[i%2]].append(w[(i+1)%2])
            else: d[w[i%2]] = [w[(i+1)%2]]
            
    for w in wires:
        cnt = 0
        visited = [False] * (n+1)
        q = deque();    q.append(1)
        
        while q:
            pl = q.popleft()
            if visited[pl] : continue
            for v in d[pl]:
                a, b = min(pl, v), max(pl, v)
                if (a == w[0] and b == w[1]) or visited[a] or visited[b] : continue
                q.append(a); q.append(b)
            visited[pl] = True
            cnt += 1
            
        answer = min(answer, abs(cnt - (n - cnt)))
            
    return answer
