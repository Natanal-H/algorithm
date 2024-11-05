# 프로그래머스 문제 풀이 - flag에 따라 다른 값 반환하기 (181933)

## 문제 정보
# **문제 이름**: flag에 따라 다른 값 반환하기
# **문제 번호**: 181933
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181933)

## 문제 
# 문제 설명 :
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 
# false면 a - b를 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(a, b, flag):
    return a + b if flag else a - b
