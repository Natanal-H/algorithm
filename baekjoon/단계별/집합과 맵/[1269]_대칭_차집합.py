# ------------------------------------------------------
# 문제 번호 : [1269] 대칭 차집합
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1269
# 난이도 : X
# 분류 : 자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵
# 날짜 : 2024-11-05
# ------------------------------------------------------

# 문제 설명 :
# 자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 
# 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 
# 두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

# 코드
A, B = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
print(len(set_A.difference(set_B) | set_B.difference(set_A)))
