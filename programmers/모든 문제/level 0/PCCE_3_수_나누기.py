# 프로그래머스 문제 풀이 - [PCCE 기출문제] 3번 / 수 나누기 (340205)

## 문제 정보
# **문제 이름**: [PCCE 기출문제] 3번 / 수 나누기
# **문제 번호**: 340205
# **문제 레벨**: 0
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340205)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 
# 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.

## 코드
number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100

print(answer)
