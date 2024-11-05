# 프로그래머스 문제 풀이 - 문자열 섞기 (181942)

## 문제 정보
# **문제 이름**: 문자열 섞기
# **문제 번호**: 181942
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181942)

## 문제 
# 문제 설명 :
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 
# return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]+str2[i]
    return answer
