# 프로그래머스 문제 풀이 - 배열 만들기 2 (181921)

## 문제 정보
# **문제 이름**: 배열 만들기 2
# **문제 번호**: 181921
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181921)
# **풀이 날짜** : 2024-11-05

## 문제 
# 문제 설명 :
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 
# 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

## 코드
def solution(l, r):
    answer = []
    if l % 5 : l += 5 - (l % 5)
    for i in range(l, r+1, 5):
        if str(i).replace('0','').replace('5','') == '': answer.append(i)
        
    return answer if answer else [-1]
