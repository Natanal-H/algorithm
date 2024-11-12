# 프로그래머스 문제 풀이 - 숫자 찾기 (120904)

## 문제 정보
# **문제 이름**: 숫자 찾기
# **문제 번호**: 120904
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120904)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고
# 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

## 코드
def solution(num, k):
    try :
        return str(num).index(str(k))+1
    except :
        return -1
