# 프로그래머스 문제 풀이 - 날짜 비교하기 (181838)

## 문제 정보
# **문제 이름**: 날짜 비교하기
# **문제 번호**: 181838
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181838)
# **풀이 날짜** : 2024-11-07

## 문제 
# 문제 설명 :
# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 
# 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
# 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.

## 코드
def solution(date1, date2):
    arr = [0, 0]
    
    for i in range(3):
        arr[0] += date1[i] * 10 ** (4 - 2 * i)
        arr[1] += date2[i] * 10 ** (4 - 2 * i)
        
    return int(arr[0] < arr[1])
