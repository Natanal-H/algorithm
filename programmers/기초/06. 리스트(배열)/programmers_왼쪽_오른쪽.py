# 프로그래머스 문제 풀이 - 왼쪽 오른쪽 (181890)

## 문제 정보
# **문제 이름**: 왼쪽 오른쪽
# **문제 번호**: 181890
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181890)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다. 
# str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return하도록 solution 함수를 완성해주세요. 
# "l"이나 "r"이 없다면 빈 리스트를 return합니다.

## 코드
def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i]=='l': 
            return str_list[:i]
        elif str_list[i]=='r': 
            return str_list[i+1:]
    return []
