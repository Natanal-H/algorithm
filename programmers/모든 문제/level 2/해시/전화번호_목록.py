# 프로그래머스 문제 풀이 - 전화번호 목록 (42577)

## 문제 정보
# **문제 이름**: 전화번호 목록
# **문제 번호**: 42577
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42577)
# **풀이 날짜** : 2024-11-25

## 문제 
# 문제 설명 :
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

## 코드
def solution(phone_book):
    pbset = set(phone_book);
    for pb in phone_book :
        for i in range(1, len(pb)):
            if pb[:i] in pbset : return False
    
    return True
