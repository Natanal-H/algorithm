# ------------------------------------------------------
# 문제 번호 : [4134] 다음 소수
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/4134
# 난이도 : X
# 분류 : 수학, 브루트포스 알고리즘, 정수론, 소수 판정
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 브루트 포스(Brute Force) 알고리즘은 문제를 해결하기 위해 가능한 모든 경우의 수를 탐색하는 방법입니다.

# 문제 설명 :
# 정수 n(0 ≤ n ≤ 4 * 10^9)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 코드
T = int(input())

def find_prime(n):
    if n <= 2 :
        return 2
    
    while True:
        i = 2
        flag = True
        
        if n % i == 0:
            n += 1
        else :
            while i**2 <= n :
                if n % i == 0 :
                    flag = False
                    break
                i += 1
            if flag : return n
            n += 2

for _ in range(T):
    n = int(input())    
    print(find_prime(n))
