# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌1] 삼각 달팽이 (68645)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌1] 삼각 달팽이
# **문제 번호**: 68645
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/68645)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    answer = []
    arr = [[0 for _ in range(i+1)]for i in range(n)]
    d, dx, dy = 0, [1,0,-1], [0,1,-1]
    idx, x, y = 1, 0, 0
    
    while idx <= n*(n+1)//2 :
        arr[x][y] = idx
        x1, y1 = x + dx[d], y + dy[d]

        if not (0<=x1<n and 0<=y1<len(arr[x1]) and arr[x1][y1]==0):
            d += 1; d %= 3
 
        x += dx[d]; y += dy[d]; idx += 1
    
    for a in arr : answer += a
    
    return answer
