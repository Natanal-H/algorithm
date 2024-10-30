# ------------------------------------------------------
# 문제 번호 : [10871] X보다 작은 수
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10871
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 코드
N, X = map(int, input().split())
A = map(int, input().split())

flag = False

for a in A :
    if a < X :
        if flag : print(' ', end='')
        else : flag = True
            
        print(a, end='')
