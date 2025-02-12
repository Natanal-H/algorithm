# 프로그래머스 문제 풀이 - [2022 KAKAO BLIND RECRUITMENT] 신고 결과 받기 (92334)

## 문제 정보
# **문제 이름**: [2022 KAKAO BLIND RECRUITMENT] 신고 결과 받기
# **문제 번호**: 92334
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/92334)
# **풀이 날짜** : 2024-11-13

## 문제 
# 문제 설명 :
# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
#
# 이용자의 ID가 담긴 문자열 배열 id_list, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 
# 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(id_list, report, k):
    d = {}
    answer = {}
    
    for i in id_list : 
        d[i] = set()
        answer[i] = 0
        
    for r in report :
        r = r.split()
        d[r[1]].add(r[0])
        
    for key, value in d.items():
        if len(value) < k : continue
        for name in value: answer[name] += 1
        
    return [v for v in answer.values()]
