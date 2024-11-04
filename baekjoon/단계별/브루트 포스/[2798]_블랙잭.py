# ------------------------------------------------------
# 문제 번호 : [2798] 블랙잭 
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2798
# 난이도 : X
# 분류 : 브루트 포스 알고리즘
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 브루트 포스(Brute Force) 알고리즘은 문제를 해결하기 위해 가능한 모든 경우의 수를 탐색하는 방법입니다.

# 문제 설명 :
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
# 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
#
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 코드
N, M = map(int, input().split())
arr = sorted(list(map(int,input().split())))

max_sum = 0

for i in range(N-2):
    if arr[i] > M : break
    
    for j in range(i+1,N-1):
        if arr[i] + arr[j] > M : break
        
        for k in range(j+1,N):
            s = arr[i] + arr[j] + arr[k]
            if s > M : break
            max_sum = max(max_sum, s)
                        
print(max_sum)
