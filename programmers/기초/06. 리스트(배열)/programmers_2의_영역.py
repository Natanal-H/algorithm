# 프로그래머스 문제 풀이 - 2의 영역 (181894)

## 문제 정보
# **문제 이름**: 2의 영역
# **문제 번호**: 181894
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181894)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

## 코드
def solution(arr):
    a = []
    
    for i in range(len(arr)):
        if arr[i] == 2:
            a.append(i)
            
    if a :
        if len(a) == 1:
            return [2]
        else :
            return arr[a[0]:a[-1]+1]
        
    return [-1]
