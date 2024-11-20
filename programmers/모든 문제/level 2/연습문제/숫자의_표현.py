# 프로그래머스 문제 풀이 - 숫자의 표현 (12924)

## 문제 정보
# **문제 이름**: 숫자의 표현
# **문제 번호**: 12924
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12924)
# **풀이 날짜** : 2024-11-20

## 문제 
# 문제 설명 :
# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

## 코드
def solution(n):
    answer = 0
    l, r, s = 1, 1, 1
    
    while l * 2 <= n :
        if s == n : 
            answer += 1
            s -= l; l += 1
            r += 1; s += r
        elif s > n :
            s -= l; l += 1
        else : 
            r += 1; s += r
    return answer + 1
