# 프로그래머스 문제 풀이 - 더 맵게 (42626)

## 문제 정보
# **문제 이름**: 더 맵게
# **문제 번호**: 42626
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42626)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

## 코드
import heapq

def solution(scoville, K):
    answer, heap = 0, []

    for s in scoville : heapq.heappush(heap, s)
    
    while len(heap) > 1:
        if heap[0] >= K : return answer
        
        h1 = heapq.heappop(heap)
        h2 = heapq.heappop(heap) 
        heapq.heappush(heap, h1 + h2*2)
        answer += 1
        
    if heap[0] >= K : return answer 
    return -1
