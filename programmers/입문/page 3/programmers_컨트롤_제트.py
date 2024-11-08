# 프로그래머스 문제 풀이 - 컨트롤 제트 (120853)

## 문제 정보
# **문제 이름**: 컨트롤 제트
# **문제 번호**: 120853
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120853)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다. 문자열에 있는 숫자를 차례대로 더하려고 합니다.
# 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(s):
    s = s.split()
    
    answer = 0
    ret = 0
    
    for v in s:
        if v == 'Z' :
            answer -= ret
        else :
            answer += int(v)
            ret = int(v)
    
    return answer
