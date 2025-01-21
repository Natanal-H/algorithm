# 프로그래머스 문제 풀이 - 호텔 대실 (155651)

## 문제 정보
# **문제 이름**: 호텔 대실
# **문제 번호**: 155651
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/155651)
# **풀이 날짜** : 2025-01-21

## 문제 
# 문제 설명 :
# 호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
# 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

## 코드
import heapq

def sti(string):
    s = string.split(":")
    return int(s[0]) * 60 + int(s[1])

def solution(book_time):
    answer = 1
    arr, h = [], []
    
    for t in book_time:
        arr.append([sti(t[0]), sti(t[1])+10])
        
    arr.sort(key=lambda x: (x[0], x[1]))
    
    for a in arr:
        if h :
            while h :
                if h[0] <= a[0] : heapq.heappop(h)
                else : heapq.heappush(h, a[1]); break
            answer = max(answer, len(h))
        else :
            heapq.heappush(h, a[1])    
    
    return answer
