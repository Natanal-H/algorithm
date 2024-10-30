# ------------------------------------------------------
# 문제 번호 : [10807] 개수 세기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10807
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-29
# ------------------------------------------------------

# 문제 설명 :
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 코드
N = int(input())
nums = map(int, input().split())
v = int(input())
count = 0

for n in nums:
    if v == n : count += 1
    
print(count)
