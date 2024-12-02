# 프로그래머스 문제 풀이 - 연속 부분 수열 합의 개수 (131701)

## 문제 정보
# **문제 이름**: 연속 부분 수열 합의 개수
# **문제 번호**: 131701
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/131701)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 
# 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 

## 코드
def solution(elements):
    s, e = set(), elements * 2
    for i in range(1, len(elements)):
        for j in range(len(elements)):
            s.add(sum(e[j:j+i]))
    s.add(sum(elements))
    return len(s)
