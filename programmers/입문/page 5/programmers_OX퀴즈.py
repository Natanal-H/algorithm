# 프로그래머스 문제 풀이 - OX퀴즈 (120907)

## 문제 정보
# **문제 이름**: OX퀴즈
# **문제 번호**: 120907
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120907)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(quiz):
    answer = []
    
    for q in quiz:
        q = q.split(' = ')
        s = sum(map(int, q[0].replace(' - ', ' + -').replace('--', '').split(' + ')))
        if s == int(q[1]) :
            answer.append("O")
        else:
            answer.append("X")
        
    return answer
