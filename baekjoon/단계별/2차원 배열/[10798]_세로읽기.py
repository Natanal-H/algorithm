# ------------------------------------------------------
# 문제 번호 : [10798] 세로읽기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10798
# 난이도 : X
# 분류 : 구현, 문자열
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 만들어진 다섯 개의 단어를 세로로 읽으려 한다. 
# 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다.
# 다음에 두 번째 글자들을 세로로 읽는다. 
# 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
#
# 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다

# 코드
arr = []

for _ in range(5):
    arr.append(input())
    
for i in range(len(max(arr, key=len))):
    for j in range(5):
        if len(arr[j]) <= i : continue
        print(arr[j][i], end='') 
