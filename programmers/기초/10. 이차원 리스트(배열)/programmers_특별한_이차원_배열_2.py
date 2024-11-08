# 프로그래머스 문제 풀이 - 특별한 이차원 배열 2 (181835)

## 문제 정보
# **문제 이름**: 특별한 이차원 배열 2
# **문제 번호**: 181835
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181835)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
# 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

## 코드
def solution(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i][j] != arr[j][i] :
                return 0
    
    return 1
