# 프로그래머스 문제 풀이 - [위클리 챌린지] 교점에 별 만들기 (87377)

## 문제 정보
# **문제 이름**: [위클리 챌린지] 교점에 별 만들기
# **문제 번호**: 87377
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/87377)
# **풀이 날짜** : 2024-12-18

## 문제 
# 문제 설명 :
# Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.
# 직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다. 이때 모든 별을 포함하는 최소 사각형을 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(line):
    s, arr, answer = set(), [], []
    minX, minY = int(1e15), int(1e15)
    maxX, maxY = int(-1e15),int(-1e15)
    
    def getDot(l1, l2):
        A, B, E = l1
        C, D, F = l2
        if A*D - B*C == 0 : return False
        x = (B*F - E*D) / (A*D - B*C)
        y = (E*C - A*F) / (A*D - B*C)
        if x%1 != 0 or y%1 != 0 : return False
        x, y = int(x), int(y)
        if (x,y) not in s :
            s.add((x, y))
            arr.append([x, y])
        return True
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if getDot(line[i], line[j]):
                minX, minY = min(minX, arr[-1][0]), min(minY, arr[-1][1])
                maxX, maxY = max(maxX, arr[-1][0]), max(maxY, arr[-1][1])
    
    answer = [['.' for _ in range(maxX-minX+1)] for _ in range(maxY-minY+1)]
    
    for x,y in arr:
        answer[maxY-y][x-minX] = "*"
    
    return ["".join(a) for a in answer]
