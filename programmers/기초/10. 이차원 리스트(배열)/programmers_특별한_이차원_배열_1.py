# 프로그래머스 문제 풀이 - 특별한 이차원 배열 1 (181833)

## 문제 정보
# **문제 이름**: 특별한 이차원 배열 1
# **문제 번호**: 181833
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181833)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

## 코드
def solution(n):  
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
