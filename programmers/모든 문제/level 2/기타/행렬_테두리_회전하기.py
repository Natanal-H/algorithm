# 프로그래머스 문제 풀이 - [2021 Dev-Matching: 웹 백엔드 개발자(상반기)] 행렬 테두리 회전하기 (77485)

## 문제 정보
# **문제 이름**: [2021 Dev-Matching: 웹 백엔드 개발자(상반기)] 행렬 테두리 회전하기
# **문제 번호**: 77485
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/77485)
# **풀이 날짜** : 2024-11-29

## 문제 
# 문제 설명 :
# rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 
# 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 
# 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.
# x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다. 
#
# 행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 
# 각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.

## 코드
def move(arr, q):
    a = [row.copy() for row in arr]
    m = len(a) * len(a[0])
    d, dx, dy = 0, [0,1,0,-1], [1,0,-1,0]
    
    q = [q[0]-1, q[1]-1, q[2]-1, q[3]-1]
    x, y = q[0], q[1]
    
    l = (q[2]-q[0] + q[3]-q[1]) * 2
    for _ in range(l):
        if not(q[0]<=x+dx[d]<=q[2] and q[1]<=y+dy[d]<=q[3]):
            d += 1
        
        x += dx[d]; y += dy[d]        
        arr[x][y] = a[x-dx[d]][y-dy[d]]
        
        m = min(m, arr[x][y])
    return m

def solution(rows, columns, queries):
    answer = []
    arr = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    
    for q in queries :
        m = move(arr, q)
        answer.append(m)
    
    return answer
