# 프로그래머스 문제 풀이 - 문자열 계산하기 (120902)

## 문제 정보
# **문제 이름**: 문자열 계산하기
# **문제 번호**: 120902
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120902)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

## 코드
def solution(my_string):
    answer = []
    l = my_string.split(' ')
    answer.append(int(l[0]))
    
    for i in range(1,len(l),2):
        n = int(l[i+1])
        if l[i] == '-':
            n *= -1
        answer.append(n)
    
    return sum(answer)
