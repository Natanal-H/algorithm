# 프로그래머스 문제 풀이 - [2019 카카오 개발자 겨울 인턴십] 튜플 (64065)

## 문제 정보
# **문제 이름**: [2019 카카오 개발자 겨울 인턴십] 튜플
# **문제 번호**: 64065
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/64065)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음을 튜플(tuple)이라고 합니다. n개의 요소를 가진 튜플을 n-튜플(n-tuple)이라고 하며, 다음과 같이 표현할 수 있습니다.
# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(s):
    answer, arr = [], []
    
    for t in s[2:-2].split('},{'):
        arr.append(list(map(int,t.split(','))))
    arr.sort(key=lambda x: len(x))
    answer.append(arr[0][0])
    
    for i in range(1, len(arr)):
        answer.append(list(set(arr[i]) - set(answer))[0])
        
    return answer
