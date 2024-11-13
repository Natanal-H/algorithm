# 프로그래머스 문제 풀이 - 옹알이 (1) (120956)

## 문제 정보
# **문제 이름**: 옹알이 (1)
# **문제 번호**: 120956
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120956)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(babbling):
    b = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(4):
            babbling[i] = babbling[i].replace(b[j], ' ')
        babbling[i] = babbling[i].strip()
    return babbling.count('')
