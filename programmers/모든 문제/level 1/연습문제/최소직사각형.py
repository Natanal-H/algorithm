# 프로그래머스 문제 풀이 - 최소직사각형 (86491)

## 문제 정보
# **문제 이름**: 최소직사각형
# **문제 번호**: 86491
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/86491)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다.
# 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

## 코드
def solution(sizes):
    w, h = 0, 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
        
    return w*h
