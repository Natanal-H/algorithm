# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [3차] 방금그곡 (17683)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [3차] 방금그곡
# **문제 번호**: 17683
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17683)
# **풀이 날짜** : 2024-11-25

## 문제 
# 문제 설명 :
# 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

## 코드
def changeToSeconds(s) :
    s = s.split(':')
    return int(s[0]) * 60 + int(s[1])

def changeToSharp(s) :
    s = list(s)
    ret = ''
    while s :
        a = s.pop(0)
        if s and s[0] == '#':
            a = a.lower()
            s.pop(0)
        ret += a
    return ret

def solution(m, musicinfos):
    answer = []
    m = changeToSharp(m)
    
    for i, musicinfo in enumerate(musicinfos) :
        mi = musicinfo.split(',')
        t = changeToSeconds(mi[1]) - changeToSeconds(mi[0])
        mi[3] = changeToSharp(mi[3])
        s = mi[3] * (t // len(mi[3]) + 1)
        if m in s[:t] :	answer.append([t, i, mi[2]])
    
    if answer : return sorted(answer, key=lambda x:(-x[0], x[1]))[0][2]
    else : return '(None)'
    
    return answer
