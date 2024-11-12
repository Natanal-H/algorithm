# 프로그래머스 문제 풀이 - 영어가 싫어요 (120894)

## 문제 정보
# **문제 이름**: 영어가 싫어요
# **문제 번호**: 120894
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120894)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
# 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

## 코드
def solution(numbers):
    dics = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
          'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
    for d in dics.keys():
        numbers = numbers.replace(d, str(dics[d]))

    return int(numbers)
