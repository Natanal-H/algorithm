# 프로그래머스 문제 풀이 - 1로 만들기 (181880)

## 문제 정보
# **문제 이름**: 1로 만들기
# **문제 번호**: 181880
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181880)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 
# 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.
# 10 / 2 = 5
# (5 - 1) / 2 = 2
# 2 / 2 = 1
# 위와 같이 3번의 나누기 연산으로 1이 되었습니다.
# 정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

## 코드
def make1(n) :
    cnt = 0
    while n > 1:
        if n % 2 : n -= 1
        n //= 2
        cnt += 1
    return cnt

def solution(num_list):
    return sum([make1(n) for n in num_list])
