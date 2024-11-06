# 프로그래머스 문제 풀이 - 할 일 목록 (181885)

## 문제 정보
# **문제 이름**: 할 일 목록
# **문제 번호**: 181885
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181885)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
# todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(todo_list, finished):
    return [todo_list[i] for i,f in enumerate(finished) if not f]
