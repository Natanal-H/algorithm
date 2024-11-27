# 프로그래머스 문제 풀이 - [2019 KAKAO BLIND RECRUITMENT] 후보키 (42890)

## 문제 정보
# **문제 이름**: [2019 KAKAO BLIND RECRUITMENT] 후보키
# **문제 번호**: 42890
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42890)
# **풀이 날짜** : 2024-11-27

## 문제 
# 문제 설명 :
# 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
#
# 릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

## 코드
def solution(relation):
    answer = 0
    r = list(zip(*relation))    
    arr = []
    
    def subset(n, l) :
        if n == len(r): arr.append(l[:]); return
        subset(n + 1, l)
        l.append(n); subset(n + 1, l); l.pop()
        
    subset(0, []); arr.pop(0)
    arr.sort(key=lambda x: len(x))
    
    def is_key(l) :
        s = set()
        for i in range(len(r[0])):
            w = ''
            for j in l :
                w += r[j][i] + "::"
            s.add(w)
        return len(r[0]) == len(s)
    
    def check(l1, l2):
        for n in l1:
            if n not in l2:
                return False
        return True
    
    while arr :
        a = arr.pop(0)
        if is_key(a) : 
            answer += 1
            for i in range(len(arr)-1,-1,-1):
                if check(a, arr[i]): arr.pop(i)
    
    return answer
