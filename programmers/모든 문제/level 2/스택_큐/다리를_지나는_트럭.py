# 프로그래머스 문제 풀이 - 다리를 지나는 트럭 (42583)

## 문제 정보
# **문제 이름**: 다리를 지나는 트럭
# **문제 번호**: 42583
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42583)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
# 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

## 코드
def solution(bridge_length, weight, truck_weights):
    answer = 0
    arr_b, arr_t = [], []
    
    while truck_weights or arr_b :
        answer += 1
        if arr_t :
            if arr_t[0] == bridge_length :
                arr_t.pop(0); arr_b.pop(0)
            for i in range(len(arr_t)) : arr_t[i] += 1
        
        if truck_weights and sum(arr_b) + truck_weights[0] <= weight:
            arr_b.append(truck_weights.pop(0))
            arr_t.append(1)
            
    return answer
