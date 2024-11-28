# 프로그래머스 문제 풀이 - [Summer/Winter Coding(~2018)] 스킬트리 (49993)

## 문제 정보
# **문제 이름**: [Summer/Winter Coding(~2018)] 스킬트리
# **문제 번호**: 49993
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/49993)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.
# 예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.
# 위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.
# 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

## 코드
def solution(skill, skill_trees):
    answer, d = 0, {}
    
    for i in range(len(skill)) : d[skill[i]] = i
    
    def check(st) :
        i = 0
        for s in st:
            if s in d:
                if d[s] == i: i += 1
                else : return 0
        return 1
    
    for st in skill_trees : answer += check(st)
    
    return answer
