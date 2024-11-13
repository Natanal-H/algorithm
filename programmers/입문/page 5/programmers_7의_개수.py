# 프로그래머스 문제 풀이 - 7의 개수 (120912)

## 문제 정보
# **문제 이름**: 7의 개수
# **문제 번호**: 120912
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120912)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(array):
    return ''.join([str(n) for n in array]).count('7')
