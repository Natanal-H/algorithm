# 프로그래머스 문제 풀이 - 조이스틱 (42860)

## 문제 정보
# **문제 이름**: 조이스틱
# **문제 번호**: 42860
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42860)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

## 코드
def solution(name):
    if len(name) == name.count('A') : return 0
    
    arr, answer = [], 1000
    s = name[0] + 'A'*(len(name)-1)
    c = min(ord(name[0])-ord('A'), ord('Z')-ord(name[0])+1)
    
    arr.append((s, c+1, len(name)-1, -1, True))
    arr.append((s, c+1, 1, 1, True))
    
    while arr :
        s, c, i, d, b = arr.pop(0)
        
        if s == name : answer = min(answer, c-1); continue
        if i == -1 : i = len(name) - 1
        elif i == len(name) : i = 0
        
        if s[i] != name[i] :
            s = s[:i] + name[i] + s[i+1:]
            c += min(ord(name[i])-ord('A'), ord('Z')-ord(name[i])+1)
            
        arr.append((s, c+1, i+d, d, b))
        if b : arr.append((s, c+1, i-d, -d, False))

    return answer
