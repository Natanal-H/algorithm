# 프로그래머스 문제 풀이 - 배열의 길이에 따라 다른 연산하기 (181854)

## 문제 정보
# **문제 이름**: 배열의 길이에 따라 다른 연산하기
# **문제 번호**: 181854
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181854)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
# arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, 
# arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(arr, n):
    for i in range((len(arr)+1)%2,len(arr),2):
        arr[i] += n
    return arr
