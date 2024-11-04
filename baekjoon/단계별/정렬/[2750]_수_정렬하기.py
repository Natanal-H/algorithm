# ------------------------------------------------------
# 문제 번호 : [2750] 수 정렬하기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2750
# 난이도 : X
# 분류 : 구현, 정렬
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 코드
N = int(input())
arr = [int(input())]

for i in range(N-1):
    n = int(input())
    
    if n > arr[i] : arr.append(n)
    elif n < arr[0] : arr = [n] + arr
    else :
        for j in range(1, i+1):
            if n < arr[j] :
                arr = arr[:j] + [n] + arr[j:]
                break
            
for i in range(N): 
    print(arr[i])
