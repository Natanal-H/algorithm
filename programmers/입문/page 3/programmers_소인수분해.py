# 프로그래머스 문제 풀이 - 소인수분해 (120852)

## 문제 정보
# **문제 이름**: 소인수분해
# **문제 번호**: 120852
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120852)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다.
# 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    answer = []
    i = 2
    
    while n > 1:
        if n % i == 0:
            n //= i
            answer.append(i)
        else :
            i += 1
    
    return sorted(list(set(answer)))
