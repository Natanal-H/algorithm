# 프로그래머스 문제 풀이 - 배열 조각하기 (181893)

## 문제 정보
# **문제 이름**: 배열 조각하기
# **문제 번호**: 181893
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181893)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 arr와 query가 주어집니다. query를 순회하면서 다음 작업을 반복합니다.
# 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
# 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.
# 위 작업을 마친 후 남은 arr의 부분 배열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr, query):
    for i in range(len(query)) :
        if i%2 :
            arr = arr[query[i]:]
        else :
            arr = arr[:query[i] + 1]
    return arr
