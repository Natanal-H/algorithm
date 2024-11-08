# 프로그래머스 문제 풀이 - 외계어 사전 (120869)

## 문제 정보
# **문제 이름**: 외계어 사전
# **문제 번호**: 120869
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120869)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 
# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(spell, dic):
    for d in dic :
        flag = True
        for s in spell :
            if not (s in d and d.count(s) == 1) :
                flag = False
                break
        if flag :
            return 1            
    
    return 2

## 다른 코드 => dic과 spell 모두 중복된 원소를 갖지 않습니다.
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
