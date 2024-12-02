# 프로그래머스 문제 풀이 - 롤케이크 자르기 (132265)

## 문제 정보
# **문제 이름**: 롤케이크 자르기
# **문제 번호**: 132265
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/132265)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 철수는 롤케이크를 두 조각으로 잘라서 동생과 한 조각씩 나눠 먹으려고 합니다. 이 롤케이크에는 여러가지 토핑들이 일렬로 올려져 있습니다. 
# 철수와 동생은 롤케이크를 공평하게 나눠먹으려 하는데, 그들은 롤케이크의 크기보다 롤케이크 위에 올려진 토핑들의 종류에 더 관심이 많습니다. 
# 그래서 잘린 조각들의 크기와 올려진 토핑의 개수에 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것으로 생각합니다.
#
# 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수로 주어질 때, 롤케이크를 공평하게 자르는 방법의 수를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(topping):
    answer = 0
    cnts, sy, so = {}, set(), set()
    
    for t in topping :
        if t in cnts.keys(): cnts[t] += 1
        else: cnts[t] = 1; so.add(t)
    
    for t in topping:
        sy.add(t)
        cnts[t] -= 1
        if cnts[t] == 0 : so.remove(t)
        if len(sy) == len(so): answer += 1
    return answer
