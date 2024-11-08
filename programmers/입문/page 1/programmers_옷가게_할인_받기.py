# 프로그래머스 문제 풀이 - 옷가게 할인 받기 (120818)

## 문제 정보
# **문제 이름**: 옷가게 할인 받기
# **문제 번호**: 120818
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120818)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(price):
    if price >= 500000 : price *= 0.8
    elif price >= 300000 : price *= 0.9
    elif price >= 100000 : price *= 0.95
    return int(price)
