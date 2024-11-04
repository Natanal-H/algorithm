# ------------------------------------------------------
# 문제 번호 : [10815] 숫자 카드
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10815
# 난이도 : X
# 분류 : 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

# 코드
N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))

N_nums.sort()

def find_num(num) :
    left = 0
    right = N-1
    
    while(left <= right) :
        mid = (left + right) // 2
        
        if N_nums[mid] == num : return 1
        elif N_nums[mid] < num : left = mid + 1
        else : right = mid - 1
        
    return 0

for m in M_nums :
    print(find_num(m), end=' ')
