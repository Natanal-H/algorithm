# 프로그래머스 문제 풀이 - 합성수 찾기 (120846)

## 문제 정보
# **문제 이름**: 합성수 찾기
# **문제 번호**: 120846
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120846)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    check = [True] * 101
    
    i = 2
    
    while i**2 <= 100:
        if check[i]:
            for j in range(2*i, 101, i):
                check[j] = False
        i += 1
    
    return check[:n+1].count(False)
