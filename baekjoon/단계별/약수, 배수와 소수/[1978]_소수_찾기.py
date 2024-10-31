# ------------------------------------------------------
# 문제 번호 : [1978] 소수 찾기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1978
# 난이도 : X
# 분류 : 수학, 정수론, 소수 판정
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 코드
N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for n in nums :
    if n == 1 : cnt -= 1
    
    for i in range(2, n):
        if i**2 > n : break
        if n % i == 0:
            cnt -= 1
            break
        
    cnt += 1
    
print(cnt)
