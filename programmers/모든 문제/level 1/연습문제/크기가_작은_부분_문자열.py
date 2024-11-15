# 프로그래머스 문제 풀이 - 크기가 작은 부분 문자열 (147355)

## 문제 정보
# **문제 이름**: 크기가 작은 부분 문자열
# **문제 번호**: 147355
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/147355)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서, 
# 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 나오는 횟수를 return하는 함수 solution을 완성하세요.

## 코드
def solution(t, p):
    answer = 0
    l = len(p); p = int(p)
    
    for i in range(len(t)-l+1):
        if int(t[i:i+l]) <= p : answer += 1
    
    return answer
