# 프로그래머스 문제 풀이 - 최빈값 구하기 (120812)

## 문제 정보
# **문제 이름**: 최빈값 구하기
# **문제 번호**: 120812
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120812)
# **풀이 날짜** : 2024-11-08

## 문제 
# 문제 설명 :
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

## 코드
def solution(array):
    arr = [0] * 1000
    
    for a in array :
        arr[a] += 1
        
    m = max(arr)
    
    print(arr[:10])
    
    return arr.index(m) if arr.count(m) == 1 else -1
