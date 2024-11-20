# 프로그래머스 문제 풀이 - 최댓값과 최솟값 (12939)

## 문제 정보
# **문제 이름**: 최댓값과 최솟값
# **문제 번호**: 12939
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/12939)
# **풀이 날짜** : 2024-11-20

## 문제 
# 문제 설명 :
# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.

## 코드
def solution(s):
    s = list(map(int, s.split()))
    return f'{min(s)} {max(s)}'
