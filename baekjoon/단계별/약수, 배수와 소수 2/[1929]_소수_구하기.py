# ------------------------------------------------------
# 문제 번호 : [1929] 소수 구하기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1929
# 난이도 : X
# 분류 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 에라토스테네스의 체(Sieve of Eratosthenes)는 체로 치듯이 수를 걸러내어 소수를 찾는 방법이다.

# 문제 설명 :
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 코드
M, N = map(int, input().split())
arr = [0] * (N + 1)

arr[1] = 1

for i in range(2, int(N ** 0.5) + 1) :
    if arr[i] : continue
    for j in range(i*2, N+1, i) :
        arr[j] += 1
        
for i in range(M, N+1):
    if not arr[i]: print(i)
