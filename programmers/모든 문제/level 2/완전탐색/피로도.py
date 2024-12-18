# 프로그래머스 문제 풀이 - 피로도 (87946)

## 문제 정보
# **문제 이름**: 피로도
# **문제 번호**: 87946
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/87946)
# **풀이 날짜** : 2024-12-18

## 문제 
# 문제 설명 :
# XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 
# 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다.
# "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 
#
# 이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 
# 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

## 코드
answer = 0
def solution(k, dungeons):    
    l = len(dungeons)
    visited = [False] * l
    
    def goDungeon(n, p, v):
        global answer
        if p < 0: return
        if n == l : answer = n; return
        answer = max(answer, n)
        
        for i in range(l):
            if not v[i] and dungeons[i][0]<=p:
                v[i] = True
                goDungeon(n+1, p-dungeons[i][1], v)
                v[i] = False
    
    goDungeon(0, k, visited)
    return answer
