# ------------------------------------------------------
# 문제 번호 : [10816] 숫자 카드 2
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10816
# 난이도 : X
# 분류 : 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 코드
import sys

N = int(input())
list_n = sys.stdin.readline().strip().split()
M = int(input())
list_m = sys.stdin.readline().strip().split()

dic = {}

for n in list_n :
    if n in dic.keys():
        dic[n] += 1
    else :
        dic[n] = 1

for m in list_m :
    if m in dic.keys():
        print(dic[m], end=' ')
    else :
        print(0, end=' ')
