# ------------------------------------------------------
# 문제 번호 : [18870] 좌표 압축
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/18870
# 난이도 : X
# 분류 : 정렬, 값 / 좌표 압축
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다. 
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 코드
N = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(list(set(X)))
dict_X = {}

for i in range(len(sorted_X)):
    dict_X[sorted_X[i]] = i

for x in X :
    print(dict_X[x], end=' ')
