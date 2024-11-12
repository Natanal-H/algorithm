# 프로그래머스 문제 풀이 - k의 개수 (120887)

## 문제 정보
# **문제 이름**: k의 개수
# **문제 번호**: 120887
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120887)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 
# 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(i, j, k):
    return sum([str(i).count(str(k)) for i in range(i,j+1)])
