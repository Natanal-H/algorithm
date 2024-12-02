# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌3] n^2 배열 자르기 (87390)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌3] n^2 배열 자르기
# **문제 번호**: 87390
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/87390)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.
# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n+1, i%n+1))
    return answer
