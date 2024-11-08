# 프로그래머스 문제 풀이 - 정사각형으로 만들기 (181830)

## 문제 정보
# **문제 이름**: 정사각형으로 만들기
# **문제 번호**: 181830
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181830)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 이차원 정수 배열 arr이 매개변수로 주어집니다. 
# arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 
# 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(arr):
    if len(arr) < len(arr[0]):
        for _ in range(len(arr[0]) - len(arr)):
            arr.append([0] * len(arr[0]))
                       
    elif len(arr) > len(arr[0]):
        for i in range(len(arr)):
            for _ in range(len(arr) - len(arr[i])):
                arr[i].append(0)
                       
    return arr
