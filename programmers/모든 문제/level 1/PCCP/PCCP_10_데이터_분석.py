# 프로그래머스 문제 풀이 - [PCCP 기출문제] 10번 / 데이터 분석 (250121)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 10번 / 데이터 분석
# **문제 번호**: 250121
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/250121)
# **풀이 날짜** : 2024-11-18

## 문제 
# 문제 설명 :
# AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다. 
# 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.
#
# 정렬한 데이터들이 담긴 이차원 정수 리스트 data와 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 ext, 뽑아낼 정보의 기준값을 나타내는 정수 val_ext, 
# 정보를 정렬할 기준이 되는 문자열 sort_by가 주어집니다.
# data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해 주세요. 
# 단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다.

## 코드
def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    answer = []
    
    for d in data :
        if d[dic[ext]] < val_ext :
            answer.append(d)
    
    return sorted(answer, key=lambda x:x[dic[sort_by]])
