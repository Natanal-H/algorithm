# 프로그래머스 문제 풀이 - 가장 가까운 같은 글자 (142086)

## 문제 정보
# **문제 이름**: 가장 가까운 같은 글자
# **문제 번호**: 142086
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/142086)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.

## 코드
def solution(s):
    answer = []
    arr = [-1] * 26
    
    for i in range(len(s)):
        a = ord(s[i]) - 97
    
        if arr[a] == -1:
            answer.append(-1)
        else :
            answer.append(i - arr[a])
        arr[a] = i
    
    return answer
