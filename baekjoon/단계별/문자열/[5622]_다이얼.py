# ------------------------------------------------------
# 문제 번호 : [5622] 다이얼
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/5622
# 난이도 : X
# 분류 : 구현
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 숫자 1을 걸려면 총 2초가 필요하다. 
# 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#
# 할머니는 전화 번호를 다이얼에 있는 각 숫자에 해당하는 문자로 외운다.
# 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 코드
s = input()
t = 0

dic = ['ABC', 'DEF', 'GHI',
       'JKL', 'MNO', 'PQRS',
       'TUV', 'WXYZ']

for i in range(len(s)) :
    for j in range(len(dic)):
        if s[i] in dic[j] :
            t += 3 + j
print(t) 
