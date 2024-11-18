# 프로그래머스 문제 풀이 - [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지 (340212)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지
# **문제 번호**: 340212
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340212)
# **풀이 날짜** : 2024-11-18

## 문제 
# 문제 설명 :
# 당신은 순서대로 n개의 퍼즐을 제한 시간 내에 풀어야 하는 퍼즐 게임을 하고 있습니다. 각 퍼즐은 난이도와 소요 시간이 정해져 있습니다. 
# 당신의 숙련도에 따라 퍼즐을 풀 때 틀리는 횟수가 바뀌게 됩니다. 현재 퍼즐의 난이도를 diff, 현재 퍼즐의 소요 시간을 time_cur, 이전 퍼즐의 소요 시간을 time_prev, 당신의 숙련도를 level이라 하면, 게임은 다음과 같이 진행됩니다.
#
# diff ≤ level이면 퍼즐을 틀리지 않고 time_cur만큼의 시간을 사용하여 해결합니다.
#
# diff > level이면, 퍼즐을 총 diff - level번 틀립니다. 퍼즐을 틀릴 때마다, time_cur만큼의 시간을 사용하며, 
# 추가로 time_prev만큼의 시간을 사용해 이전 퍼즐을 다시 풀고 와야 합니다. 이전 퍼즐을 다시 풀 때는 이전 퍼즐의 난이도에 상관없이 틀리지 않습니다. 
# diff - level번 틀린 이후에 다시 퍼즐을 풀면 time_cur만큼의 시간을 사용하여 퍼즐을 해결합니다.
#
# 퍼즐 게임에는 전체 제한 시간 limit가 정해져 있습니다. 제한 시간 내에 퍼즐을 모두 해결하기 위한 숙련도의 최솟값을 구하려고 합니다. 난이도, 소요 시간은 모두 양의 정수며, 숙련도도 양의 정수여야 합니다.

## 코드
def check(d, t, l, v):
    s = (max(0, d[0] - v) + 1) * t[0]
    for i in range(1, len(d)):
        s += max(0, d[i] - v) * (t[i] + t[i-1]) + t[i]
        if s > l : return False
    return True  

def solution(diffs, times, limit):    
    left = 1
    right = max(diffs)
    
    while left <= right :
        mid = (left + right) // 2
        A = check(diffs, times, limit, mid)
        B = check(diffs, times, limit, mid + 1)
        if not A and B : return mid+1
        elif A and B : right = mid-1
        else : left = mid+1      
    
    return 1
