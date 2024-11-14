# 프로그래머스 문제 풀이 - 삼총사 (131705)

## 문제 정보
# **문제 이름**: 삼총사
# **문제 번호**: 131705
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/131705)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다.
#
# 한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

## 코드
def solution(number):
    answer = 0
    number.sort()
    l = len(number)
    
    for i in range(l-2):
        s = number[i]
        for j in range(i+1, l-1):
            s += number[j]
            for k in range(j+1, l):
                if s + number[k] > 0 : break
                if s + number[k] == 0 : answer += 1
            s -= number[j]
    
    return answer

## 다른 코드
def solution (number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt
