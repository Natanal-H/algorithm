# 프로그래머스 문제 풀이 - 배열의 원소 삭제하기 (181844)

## 문제 정보
# **문제 이름**: 배열의 원소 삭제하기
# **문제 번호**: 181844
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181844)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 배열 arr과 delete_list가 있습니다. 
# arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(arr, delete_list):
    arr = sorted([[i, v] for i, v in enumerate(arr)], key=lambda x: x[1] )
    delete_list = sorted(delete_list)
    
    i = j = 0
    
    while i < len(arr) and j < len(delete_list):
        if arr[i][1] == delete_list[j] :
            arr.pop(i)
        elif arr[i][1] > delete_list[j] :
            j += 1
        else :
            i += 1
            
    arr = sorted([a for a in arr], key=lambda x: x[0] )

    return [a[1] for a in arr]

## 다른 코드
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]
