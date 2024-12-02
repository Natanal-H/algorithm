# 프로그래머스 문제 풀이 - 귤 고르기 (138476)

## 문제 정보
# **문제 이름**: 귤 고르기
# **문제 번호**: 138476
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/138476)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다.
# 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
#
# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 
# 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

## 코드
def solution(k, tangerine):
    d, s = {}, 0
    for t in tangerine:
        if t in d : d[t] += 1
        else : d[t] = 1
    d = sorted([list(kv) for kv in d.items()], reverse=True, key=lambda x:x[1])
    for i in range(len(d)):
        s += d[i][1]
        if k <= s: return i+1
