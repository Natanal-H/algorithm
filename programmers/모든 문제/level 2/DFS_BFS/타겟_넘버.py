# 프로그래머스 문제 풀이 - 타겟 넘버 (43165)

## 문제 정보
# **문제 이름**: 타겟 넘버
# **문제 번호**: 43165
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/43165)
# **풀이 날짜** : 2024-11-27

## 문제 
# 문제 설명 :
# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 코드
def solution(numbers, target):  
    def dfs(i, s) :
        if i == len(numbers): return int(s == target)
        return dfs(i+1,s+numbers[i]) + dfs(i+1,s-numbers[i])
        
    return dfs(0, 0)
