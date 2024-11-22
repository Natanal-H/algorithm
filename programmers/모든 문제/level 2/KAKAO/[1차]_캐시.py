# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [1차] 캐시 (17680)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [1차] 캐시
# **문제 번호**: 17680
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17680)
# **풀이 날짜** : 2024-11-22

## 문제 
# 문제 설명 :
# 지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
# 이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 
# 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
# 어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.
#
# 어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.

## 코드
def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    while cities :
        city = cities.pop(0).lower()
        
        if city in cache : 
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)
        else :
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize : cache.pop(0)
        
    return answer
