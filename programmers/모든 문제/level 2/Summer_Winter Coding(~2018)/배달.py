# 프로그래머스 문제 풀이 - [Summer/Winter Coding(~2018)] 배달 (12978)

## 문제 정보
# **문제 이름**: [Summer/Winter Coding(~2018)] 배달
# **문제 번호**: 12978
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12978)
# **풀이 날짜** : 2024-11-22

## 문제 
# 문제 설명 :
# N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다. 
# 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다. 
# 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다. 
# 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.
#
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

## 코드 : 다익스트라 알고리즘
def solution(N, road, K):
    MAX = 500001
    a = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    b = [MAX for _ in range(N+1)] 
    b[1], c = 0, [1]
    
    for x, y, n in road :
        a[x][y], a[y][x] = min(a[x][y], n), min(a[y][x], n)
    
    while c :
        idx = c.pop(0)
        for i in range(1, N+1): 
            if a[idx][i] != MAX and b[i] > b[idx] + a[idx][i]:
                b[i] = b[idx] + a[idx][i]
                c.append(i)
            
    return len([i for i in b if i <= K])
