# 프로그래머스 문제 풀이 - [2021 카카오 채용연계형 인턴십] 숫자 문자열과 영단어 (81301)

## 문제 정보
# **문제 이름**: [2021 카카오 채용연계형 인턴십] 숫자 문자열과 영단어
# **문제 번호**: 81301
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/81301)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(s):
    d = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
        'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'zero' : '0'}
    for k, v in d.items() : s = s.replace(k, v)
    return int(s)
