# 프로그래머스 문제 풀이 - 문자열이 몇 번 등장하는지 세기 (181871)

## 문제 정보
# **문제 이름**: 문자열이 몇 번 등장하는지 세기
# **문제 번호**: 181871
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181871)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(myString, pat):
    answer = 0
        
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            answer += 1
    
    return answer
