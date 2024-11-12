# 프로그래머스 문제 풀이 - 인덱스 바꾸기 (120895)

## 문제 정보
# **문제 이름**: 인덱스 바꾸기
# **문제 번호**: 120895
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120895)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
# my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(my_string, num1, num2):
    if num1 > num2 : num1, num2 = num2, num1
    return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]
