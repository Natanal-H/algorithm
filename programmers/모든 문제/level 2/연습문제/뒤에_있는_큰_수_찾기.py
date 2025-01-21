# 프로그래머스 문제 풀이 - 뒤에 있는 큰 수 찾기 (154539)

## 문제 정보
# **문제 이름**: 뒤에 있는 큰 수 찾기
# **문제 번호**: 154539
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/154539)
# **풀이 날짜** : 2025-01-21

## 문제 
# 문제 설명 :
# 정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

## 코드
def solution(numbers):
    answer = [-1] * len(numbers)
    arr = [numbers[-1]]
    
    for i in range(len(numbers)-2, -1, -1):
        while len(arr):
            if arr[-1] <= numbers[i]: arr.pop()
            else: answer[i] = arr[-1]; break
            
        arr.append(numbers[i])       
            
    return answer
