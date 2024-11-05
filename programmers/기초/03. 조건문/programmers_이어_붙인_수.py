# 프로그래머스 문제 풀이 - 이어 붙인 수 (181928)

## 문제 정보
# **문제 이름**: 이어 붙인 수
# **문제 번호**: 181928
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181928)

## 문제 
# 문제 설명 :
# 정수가 담긴 리스트 num_list가 주어집니다. 
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(num_list):
    o = ''; e = ''
    
    for n in num_list :
        if n % 2 : o += str(n)
        else : e += str(n)

    return int(o) + int(e)
