# 프로그래머스 문제 풀이 - 문자 개수 세기 (181902)

## 문제 정보
# **문제 이름**: 문자 개수 세기
# **문제 번호**: 181902
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181902)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, 
# my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수,
# my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 
# 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(my_string):
    answer = [0] * 52
    
    for s in my_string:
        if s >= 'a':
            answer[ord(s)-ord('a')+26] += 1
        else :
            answer[ord(s)-ord('A')] += 1    
    
    return answer
