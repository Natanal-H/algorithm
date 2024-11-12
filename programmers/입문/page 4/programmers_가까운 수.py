# 프로그래머스 문제 풀이 - 가까운 수 (120890)

## 문제 정보
# **문제 이름**: 가까운 수
# **문제 번호**: 120890
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120890)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(array, n):
    return sorted(array, key=lambda x: (abs(x-n),x))[0]
