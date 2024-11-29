# 프로그래머스 문제 풀이 - [2021 KAKAO BLIND RECRUITMENT] 순위 검색 (72412)

## 문제 정보
# **문제 이름**: [2021 KAKAO BLIND RECRUITMENT] 순위 검색
# **문제 번호**: 72412
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/72412)
# **풀이 날짜** : 2024-11-29

## 문제 
# 문제 설명 :
# 카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다. 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.
# 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
# 인재영입팀에 근무하고 있는 니니즈는 코딩테스트 결과를 분석하여 채용에 참여한 개발팀들에 제공하기 위해 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
# [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
#
# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
# 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## 코드
import bisect

def solution(info, query):
    answer, d = [], {}
    
    for i in info:
        i = i.split()
        t = tuple(i[:4])
        if t in d : d[t].append(int(i[4]))
        else : d[t] = [int(i[4])]
    
    for k, v in d.items():
        d[k] = sorted(v)
    
    for q in query:
        cnt = 0
        q = [_ for _ in q.split() if _ != 'and' and _ != '-']
        s = int(q.pop())
        for k, v in d.items():
            if len(set(k).intersection(q)) == len(q):
                cnt += len(v) - bisect.bisect_left(v, s)
        answer.append(cnt)
    
    return answer
