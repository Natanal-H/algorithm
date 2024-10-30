# ------------------------------------------------------
# 문제 번호 : [10809] 알파벳 찾기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10809
# 난이도 : X
# 분류 : 구현, 문자열
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 코드
S = input()
alpha = 'a'

while ord(alpha) <= ord('z'):
    res = -1
    for i in range(len(S)) :
        if S[i] == alpha :
            res = i
            break
    print(res, end='')
    if alpha != 'z' : print(" ", end='')
    alpha = chr(ord(alpha) + 1)
