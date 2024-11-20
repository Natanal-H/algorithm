# 프로그래머스 문제 풀이 - 땅따먹기 (12913)

## 문제 정보
# **문제 이름**: 땅따먹기
# **문제 번호**: 12913
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12913)
# **풀이 날짜** : 2024-11-20

## 문제 
# 문제 설명 :
# 땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

## 코드
def solution(land):
    for n in range(1, len(land)) :
        for i in range(4):
            v = land[n][i]
            for j in range(4):
                if i==j : continue
                land[n][i] = max(land[n][i], v + land[n-1][j])
                
    return max(land[-1])
