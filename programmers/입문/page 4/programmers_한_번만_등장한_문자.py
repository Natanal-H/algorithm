# 프로그래머스 문제 풀이 - 한 번만 등장한 문자 (120896)

## 문제 정보
# **문제 이름**: 한 번만 등장한 문자
# **문제 번호**: 120896
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120896)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

## 코드
def solution(s):
    answer = ''
    for i in range(ord('a'), ord('z') + 1):
        if s.count(chr(i)) == 1:
            answer += chr(i)
    return answer
