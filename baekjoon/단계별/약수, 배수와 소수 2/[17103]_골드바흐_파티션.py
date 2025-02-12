# ------------------------------------------------------
# 문제 번호 : [17103] 골드바흐 파티션
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/17103
# 난이도 : X
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 에라토스테네스의 체(Sieve of Eratosthenes)는 체로 치듯이 수를 걸러내어 소수를 찾는 방법이다.

# 문제 설명 :
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
# 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 코드
N = 1000000
arr = [True] * (N + 1)

for i in range(2, int(N**0.5)+1):
    if arr[i] :      
        for j in range(i*2, N+1, i) :
            arr[j] = False
            
T = int(input())

for _ in range(T):
    N = int(input())
    cnt = 0
    
    if N == 4 : cnt = 1
    
    i = 3
    while i <= N-i :
        if arr[i] and arr[N-i] :
            cnt += 1
        i += 2
    print(cnt)
