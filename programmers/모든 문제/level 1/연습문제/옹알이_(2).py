# 프로그래머스 문제 풀이 - 옹알이 (2) (133499)

## 문제 정보
# **문제 이름**: 옹알이 (2)
# **문제 번호**: 133499
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/133499)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(babbling):
    answer = 0
    l = ["aya", "ye", "woo", "ma"]
    
    def check(s):
        for i in range(4) :
            if l[i]*2 in s:
                return 0
        for i in range(4) :
            s = s.replace(l[i], ' ')
        if s.strip() == '': return 1
        return 0
    
    for b in babbling :
        answer += check(b)
    return answer
