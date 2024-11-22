# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [1차] 뉴스 클러스터링 (17677)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [1차] 뉴스 클러스터링
# **문제 번호**: 17677
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17677)
# **풀이 날짜** : 2024-11-22

## 문제 
# 문제 설명 :
# 유사한 기사를 묶는 기준을 정하기 위해서 논문과 자료를 조사하던 튜브는 "자카드 유사도"라는 방법을 찾아냈다.
# 자카드 유사도는 집합 간의 유사도를 검사하는 여러 방법 중의 하나로 알려져 있다. 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
# 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 

## 코드
import re

def divide(s):
    List = []
    for i in range(len(s)-1):
        if 'a'<=s[i]<='z' and 'a'<=s[i+1]<='z':
            List.append(s[i:i+2])
    return List

def solution(str1, str2):
    M = 65536
    s1 = re.sub(r'[^a-z]', ' ', str1.lower())
    s2 = re.sub(r'[^a-z]', ' ', str2.lower())
    l1, l2 = sorted(divide(s1)), sorted(divide(s2))
    
    if len(l1) == 0 and len(l2) == 0 : return M
    if len(l1) == 0 or len(l2) == 0 : return 0

    n, u = 0, 0    
    while l1 and l2 :
        if l1[0] == l2[0] :
            n += 1; u += 1
            l1.pop(0); l2.pop(0)
            continue
        elif l1[0] > l2[0] :
            l2.pop(0)
        else :
            l1.pop(0)
        u += 1
    u += max(len(l1), len(l2))
    
    return int((n / u) * M)
