# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌1] 3진법 뒤집기 (68935)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌1] 3진법 뒤집기
# **문제 번호**: 68935
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/68935)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(n):
    if n == 0: return 0
    
    answer = []
    
    while n > 0:
        answer.append(str(n % 3))
        n = n // 3
        
    answer = int(''.join(answer))
    i = 0
    
    while answer > 0:
        n += (answer%10) * (3**i)
        answer //= 10
        i += 1
        
    return n
