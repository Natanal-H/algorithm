# 프로그래머스 문제 풀이 - 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기 (181872)

## 문제 정보
# **문제 이름**: 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# **문제 번호**: 181872
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181872)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(myString, pat):
    l = len(pat)
    for i in range(len(myString)-l+1):
        if myString[-l-i:][:l] == pat :
            return myString[:len(myString)-i]

## 다른 코드
def solution(myString, pat):
    idx = myString[::-1].index(pat[::-1])
    return myString[:len(myString)-idx]

def solution(myString, pat):
    return myString[:myString.rfind(pat) + len(pat)]

# rfind()
# 파이썬 문자열에서 사용하는 메서드로, 주어진 문자열을 뒤에서부터 찾아서 그 위치를 반환합니다. 
# 이 메서드는 문자열 내에서 특정 서브 문자열이 마지막으로 등장하는 인덱스를 찾습니다. 만약 서브 문자열이 문자열에 없으면 -1을 반환합니다.
