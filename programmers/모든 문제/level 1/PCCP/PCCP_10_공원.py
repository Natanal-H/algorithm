# 프로그래머스 문제 풀이 - [PCCP 기출문제] 10번 / 공원 (340213)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 10번 / 공원
# **문제 번호**: 340213
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340213)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 지민이는 다양한 크기의 정사각형 모양 돗자리를 가지고 공원에 소풍을 나왔습니다. 공원에는 이미 돗자리를 깔고 여가를 즐기는 사람들이 많아 지민이가 깔 수 있는 
# 가장 큰 돗자리가 어떤 건지 확인하려 합니다.
#
# 지민이가 가진 돗자리들의 한 변의 길이들이 담긴 정수 리스트 mats, 현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트 park가 주어질 때 지민이가 
# 깔 수 있는 가장 큰 돗자리의 한 변 길이를 return 하도록 solution 함수를 완성해 주세요. 아무런 돗자리도 깔 수 없는 경우 -1을 return합니다.

## 코드
def solution(mats, park):
    m = 0
    arr = [[0 for _ in range(len(park[0])+1)] for _ in range(len(park)+1)]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] != '-1' : continue
            arr[i+1][j+1] = min(arr[i][j], arr[i][j+1], arr[i+1][j]) + 1
            m = max(m, arr[i+1][j+1])

    mats.sort(reverse=True)
    for mat in mats:
        if mat <= m : return mat
    
    return -1
