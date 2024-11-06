# 프로그래머스 문제 풀이 - 배열 만들기 3 (181895)

## 문제 정보
# **문제 이름**: 배열 만들기 3
# **문제 번호**: 181895
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181895)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
# intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
# 이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(arr, intervals):
    answer = []
    
    for s, e in intervals:
        answer += arr[s:e+1]
    
    return answer
