# 프로그래머스 문제 풀이 - 행렬의 곱셈 (12949)

## 문제 정보
# **문제 이름**: 행렬의 곱셈
# **문제 번호**: 12949
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12949)
# **풀이 날짜** : 2024-11-21

## 문제 
# 문제 설명 :
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

## 코드
def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    
    return answer
