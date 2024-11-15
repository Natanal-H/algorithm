# 프로그래머스 문제 풀이 - 추억 점수 (176963)

## 문제 정보
# **문제 이름**: 추억 점수
# **문제 번호**: 176963
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/176963)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 사진들을 보며 추억에 젖어 있던 루는 사진별로 추억 점수를 매길려고 합니다. 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됩니다.
#
# 그리워하는 사람의 이름을 담은 문자열 배열 name, 각 사람별 그리움 점수를 담은 정수 배열 yearning,
# 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때, 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.

## 코드
def solution(name, yearning, photo):
    answer = []
    
    for f in photo:
        s = 0
        for i in range(len(name)):
            if name[i] in f :
                s += yearning[i]
        answer.append(s)
    
    return answer
