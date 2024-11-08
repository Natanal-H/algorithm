# 프로그래머스 문제 풀이 - 다항식 더하기 (120863)

## 문제 정보
# **문제 이름**: 다항식 더하기
# **문제 번호**: 120863
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120863)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.

## 코드
def solution(polynomial):
    answer = ''
    x = k = 0
    string = polynomial.split('+')
    
    for s in string :
        s = s.strip()

        if s[-1] == 'x' :
            if len(s) == 1 :
                x += 1
            else :
                x += int(s[:-1])
        else :
            k += int(s)
    
    if x : 
        if x == 1:
            answer += 'x'
        else :
            answer += f'{str(x)}x'
    if x and k : answer += ' + '
    if k : answer += f'{str(k)}'
    
    return answer
