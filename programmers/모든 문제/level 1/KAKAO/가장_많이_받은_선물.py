# 프로그래머스 문제 풀이 - [2024 KAKAO WINTER INTERNSHIP] 가장 많이 받은 선물 (258712)

## 문제 정보
# **문제 이름**: [2024 KAKAO WINTER INTERNSHIP] 가장 많이 받은 선물
# **문제 번호**: 258712
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/258712)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 
# 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.
#
# 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
#
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
# 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
# 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
#
# 친구들의 이름을 담은 1차원 문자열 배열 friends 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수로 주어집니다. 
# 이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

## 코드
def solution(friends, gifts):
    l = len(friends)
    dic = {}
    arr = [[0 for _ in range(l)] for _ in range(l)]
    present = [0] * l
    result = [0] * l
    
    for i, f in enumerate(friends) : dic[f] = i
    for g in gifts :
        gs = g.split()
        arr[dic[gs[0]]][dic[gs[1]]] += 1
    for i in range(l):
        p = 0
        for j in range(l):
            p += arr[i][j] - arr[j][i]
        present[i] = p
        
    for i in range(l):
        for j in range(i+1,l):
            if arr[i][j] > arr[j][i] : result[i] += 1
            elif arr[i][j] < arr[j][i] : result[j] += 1
            elif present[i] > present[j] : result[i] += 1
            elif present[i] < present[j] : result[j] += 1          
                
    return max(result)
