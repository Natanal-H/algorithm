# 프로그래머스 문제 풀이 - 등수 매기기 (120882)

## 문제 정보
# **문제 이름**: 등수 매기기
# **문제 번호**: 120882
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120882)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 
# 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(score):
    answer = [0] * len(score)
    avgs = [[sum(score[i])/2, i] for i in range(len(score))]
    avgs = sorted(avgs, key=lambda x : x[0], reverse=True)
    
    s, g = -1, 1
    for i, avg in enumerate(avgs):
        if s == avg[0] :
            answer[avg[1]] = g
        else :
            answer[avg[1]] = i+1
            s = avg[0]
            g = i+1

    return answer
  
## 다른 코드
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
