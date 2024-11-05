# 프로그래머스 문제 풀이 - 문자열 반복해서 출력하기 (181950)

## 문제 정보
# **문제 이름**: 문자열 반복해서 출력하기
# **문제 번호**: 181950
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181950)

## 문제 
# 문제 설명 :
# 문자열 str과 정수 n이 주어집니다.
# str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

## 코드
str, n = input().strip().split(' ')
print(str*int(n))
