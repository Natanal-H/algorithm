# 프로그래머스 문제 풀이 - 큰 수 만들기 (42883)

## 문제 정보
# **문제 이름**: 큰 수 만들기
# **문제 번호**: 42883
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42883)
# **풀이 날짜** : 2024-11-27

## 문제 
# 문제 설명 :
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

## 코드
def solution(number, k):
    answer = ''
    while k > 0 :
        if k == len(number): break
        m = '0'
        i = 0
        for idx in range(k+1):
            if number[idx] == '9':
                m = '9'; i = idx; break
            if number[idx] > m :
                m = number[idx]; i = idx
        answer += m
        number = number[i+1:]
        k -= i
        if k == 0 : answer += number
    
    return answer
