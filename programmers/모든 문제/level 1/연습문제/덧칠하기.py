# 프로그래머스 문제 풀이 - 덧칠하기 (161989)

## 문제 정보
# **문제 이름**: 덧칠하기
# **문제 번호**: 161989
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/161989)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 어느 학교에 페인트가 칠해진 길이가 n미터인 벽이 있습니다.  벽을 1미터 길이의 구역 n개로 나누고, 각 구역에 왼쪽부터 순서대로 1번부터 n번까지 번호를 붙였습니다. 
# 그리고 페인트를 다시 칠해야 할 구역들을 정했습니다.
# 한 구역에 페인트를 여러 번 칠해도 되고 다시 칠해야 할 구역이 아닌 곳에 페인트를 칠해도 되지만 다시 칠하기로 정한 구역은 적어도 한 번 페인트칠을 해야 합니다.
# 예산을 아끼기 위해 다시 칠할 구역을 정했듯 마찬가지로 롤러로 페인트칠을 하는 횟수를 최소화하려고 합니다.
# 정수 n, m과 다시 페인트를 칠하기로 정한 구역들의 번호가 담긴 정수 배열 section이 매개변수로 주어질 때 롤러로 페인트칠해야 하는 최소 횟수를 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(n, m, section):
    answer = 0
    arr = [False] * (n+1)
    for s in section: arr[s] = True
    for i in range(n+1):
        if arr[i]:
            for j in range(m):
                if i+j >= len(arr): break
                arr[i+j] = False
            answer += 1
    
    return answer

## 다른 코드
def solution(n, m, section):
    n = 0
    k = 0
    for s in section:
        if s > k:
            n += 1
            k = s+m-1
    return n
