# 프로그래머스 문제 풀이 - 달리기 경주 (178871)

## 문제 정보
# **문제 이름**: 달리기 경주
# **문제 번호**: 178871
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/178871)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 
#
# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

## 코드
def solution(players, callings):
    d = {}
    for i in range(len(players)):
        d[i+1] = players[i]
        d[players[i]] = i+1
        
    for c in callings :
        f, g = d[d[c] - 1], d[c]
        d[c], d[f] = d[f], d[c]
        d[g], d[g - 1] = d[g - 1], d[g]
        
    return [d[i] for i in range(1, len(players)+1)]
