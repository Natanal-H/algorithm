# 프로그래머스 문제 풀이 - 외계행성의 나이 (120834)

## 문제 정보
# **문제 이름**: 외계행성의 나이
# **문제 번호**: 120834
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120834)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(age):
    return ''.join([chr(ord(a)-ord('0')+ord('a')) for a in str(age)])
