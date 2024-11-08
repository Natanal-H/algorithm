# 프로그래머스 문제 풀이 - 진료순서 정하기 (120835)

## 문제 정보
# **문제 이름**: 진료순서 정하기
# **문제 번호**: 120835
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120835)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

## 코드
def solution(emergency):
    arr = sorted(emergency, reverse=True)
    answer = [0] * len(arr)
    
    for i in range(len(arr)):
        answer[emergency.index(arr[i])] = i+1
        
    return answer
