# 프로그래머스 문제 풀이 - [2020 KAKAO BLIND RECRUITMENT] 괄호 변환 (60058)

## 문제 정보
# **문제 이름**: [2020 KAKAO BLIND RECRUITMENT] 괄호 변환
# **문제 번호**: 60058
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/60058)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 카카오에 신입 개발자로 입사한 "콘"은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다. 
# 소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
# 수정해야 할 소스 파일이 너무 많아서 고민하던 "콘"은 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.

## 코드
def solution(p):
    d = {'(':1, ')':-1}
    
    def parentheses(w):
        if w == '' : return ''
        cnt, idx = d[w[0]], 0
        for i in range(1, len(w)) :
            cnt += d[w[i]]
            if cnt == 0: idx = i; break
        
        if d[w[0]] == 1: return w[:idx+1] + parentheses(w[idx+1:])
        else :
            ret = '(' + parentheses(w[idx+1:]) + ')'
            for i in range(1, idx):
                if w[i] == '(' : ret += ')'
                else : ret += '('
            return ret
            
    return parentheses(p)
