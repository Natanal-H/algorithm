# 프로그래머스 문제 풀이 - 둘만의 암호 (155652)

## 문제 정보
# **문제 이름**: 둘만의 암호
# **문제 번호**: 155652
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/155652)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.
# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
# skip에 있는 알파벳은 제외하고 건너뜁니다.

## 코드
def solution(s, skip, index):
    answer = ''
    
    for a in s :
        i = 0
        while i < index:
            a = chr((ord(a) - 97 + 1) % 26 + 97)
            if a in skip : continue
            i += 1
        answer += a
    
    return answer
