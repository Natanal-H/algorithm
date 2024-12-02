# 프로그래머스 문제 풀이 - 우박수열 정적분 (134239)

## 문제 정보
# **문제 이름**: 우박수열 정적분
# **문제 번호**: 134239
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/134239)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 콜라츠 추측이란 로타르 콜라츠(Lothar Collatz)가 1937년에 제기한 추측으로 모든 자연수 k에 대해 다음 작업을 반복하면 항상 1로 만들 수 있다는 추측입니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2.결과로 나온 수가 1보다 크다면 1번 작업을 반복합니다.
#
# 우박수의 초항 k와, 정적분을 구하는 구간들의 목록 ranges가 주어졌을 때 정적분의 결과 목록을 return 하도록 solution을 완성해주세요. 단, 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의합니다.

## 코드
def solution(k, ranges):
    answer, arr, a = [], [k], []
    
    while k != 1 :
        if k % 2 : k = 3*k + 1
        else : k //= 2
        arr.append(k)
        a.append((arr[-1]+arr[-2])/2)

    for r in ranges:
        x1, x2 = r[0], len(a)+r[1]
        if x1 > x2 : answer.append(-1.0)
        elif x1 == x2 : answer.append(0.0)
        else : 
            answer.append(sum(a[x1:x2]))
    
    return answer
