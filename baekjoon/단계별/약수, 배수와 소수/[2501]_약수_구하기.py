# ------------------------------------------------------
# 문제 번호 : [2501] 약수 구하기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2501
# 난이도 : X
# 분류 : 수학, 브루트포스 알고리즘
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

# 코드
N, K = map(int, input().split())

arr = []
i = 1

while i ** 2 <= N :
    if N % i == 0 :
        arr.append(i)
        if i**2 != N :
            arr.append(N // i)
    i += 1

arr.sort()
if len(arr) < K :
    print(0)
else:
    print(arr[K-1])
