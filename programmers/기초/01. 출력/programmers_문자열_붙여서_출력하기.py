# 프로그래머스 문제 풀이 - 문자열 붙여서 출력하기 (181946)

## 문제 정보
# **문제 이름**: 문자열 붙여서 출력하기
# **문제 번호**: 181946
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181946)

## 문제 
# 문제 설명 :
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 입력 #1
# apple pen
# 출력 #1
# applepen

## 코드
str1, str2 = input().strip().split(' ')
print(str1 + str2)
