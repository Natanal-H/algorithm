# ------------------------------------------------------
# 문제 번호 : [2581] 소수
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2581
# 난이도 : X
# 분류 : 수학, 정수론, 소수 판정
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라
# 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 코드
M = int(input())
N = int(input())

arr = []

for n in range(M, N+1) :
    if n == 1 : continue
    if n == 2 : arr.append(2); continue
    
    for i in range(2, n):
        if i**2 > n :
            arr.append(n)
            break
        if n % i == 0: break
        
if len(arr) > 0 :
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
