# 프로그래머스 문제 풀이 - N-Queen (12952)

## 문제 정보
# **문제 이름**: N-Queen
# **문제 번호**: 12952
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12952)
# **풀이 날짜** : 2024-11-21

## 문제 
# 문제 설명 :
# 가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.
# 체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때, n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.

## 코드
def solution(N):
    answer = 0
    
    def check(l, n, index):
        for i in range(N):
            if l[i] == 0: continue
            if abs(l[i] - n) == abs(i - index): 
                return False
        return True
    
    def queen(l, n):
        nonlocal answer
        if n == 0 : 
            answer += 1
            return
        
        for i in range(N) :
            if l[i] == 0 and check(l, n, i):
                l[i] = n
                queen(l, n-1)
                l[i] = 0
        
    queen([0] * N, N)
    
    return answer
