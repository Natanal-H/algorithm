# 프로그래머스 문제 풀이 - 배열 만들기 5 (181912)

## 문제 정보
# **문제 이름**: 배열 만들기 5
# **문제 번호**: 181912
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181912)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
# 배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
# 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs :
        if int(num[s:s+l]) > k :
            answer.append(int(num[s:s+l]))
    return answer
