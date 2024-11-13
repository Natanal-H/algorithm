# 프로그래머스 문제 풀이 - [PCCE 기출문제] 5번 / 산책 (250129)

## 문제 정보
# **문제 이름**: [PCCE 기출문제] 5번 / 산책
# **문제 번호**: 250129
# **문제 레벨**: 0
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/250129)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 여름이는 강아지를 산책시키려고 합니다. 여름이는 2차원 좌표평면에서 동/서/남/북 방향으로 1m 단위로 이동하면서 강아지를 산책시킵니다. 
# 산책루트가 담긴 문자열 route가 주어질 때, 도착점의 위치를 return하도록 빈칸을 채워 solution함수를 완성해 주세요.

## 코드
def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :
            east += 1
        elif i == "W" :
            east -= 1
    return [east, north]
