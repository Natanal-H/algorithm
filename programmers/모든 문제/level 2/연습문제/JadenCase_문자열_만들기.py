# 프로그래머스 문제 풀이 - JadenCase 문자열 만들기 (12951)

## 문제 정보
# **문제 이름**: JadenCase 문자열 만들기
# **문제 번호**: 12951
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12951)
# **풀이 날짜** : 2024-11-21

## 문제 
# 문제 설명 :
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

## 코드
def solution(s):
    s = s.lower()
    flag = True
    
    for i in range(len(s)):
        if s[i] != ' ' :
            if flag :
                s = s[:i] + s[i].upper() + s[i+1:]
                flag = False
        else :
            flag = True
    
    return s
