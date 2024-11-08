# 프로그래머스 문제 풀이 - 분수의 덧셈 (120808)

## 문제 정보
# **문제 이름**: 분수의 덧셈
# **문제 번호**: 120808
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120808)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

## 코드
import math

def solution(numer1, denom1, numer2, denom2):
    s = numer1 * denom2 + denom1 * numer2
    m = denom1 * denom2
    g = math.gcd(s, m)
    return [s // g, m // g]
