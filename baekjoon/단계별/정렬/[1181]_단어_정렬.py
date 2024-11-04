# ------------------------------------------------------
# 문제 번호 : [1181] 단어 정렬
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1181
# 난이도 : X
# 분류 : 문자열, 정렬
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 코드
import sys

N = int(input())
arr = {}

for _ in range(N):
    s = sys.stdin.readline().strip()
    
    if len(s) in arr.keys() :
        if s not in arr[len(s)] :
            arr[len(s)] += [s]
    else :
        arr[len(s)] = [s]
    
for i in range(1,51):
    if i in arr.keys() :
        words = sorted(arr[i])
        [print(w) for w in words]

# import sys
# 
# data = sys.stdin.read().split('\n')
# words = list(set(data[1:-1]))
# words.sort(key=lambda x: (len(x), x))
# for w in words:
#     print(w)
