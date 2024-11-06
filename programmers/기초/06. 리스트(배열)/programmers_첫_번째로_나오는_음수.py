# 프로그래머스 문제 풀이 - 첫 번째로 나오는 음수 (181896)

## 문제 정보
# **문제 이름**: 첫 번째로 나오는 음수
# **문제 번호**: 181896
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181896)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

## 코드
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0 : return i
    return -1
