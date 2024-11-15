# 프로그래머스 문제 풀이 - [PCCP 기출문제] 1번 / 동영상 재생기 (340213)

## 문제 정보
# **문제 이름**: [PCCP 기출문제] 1번 / 동영상 재생기
# **문제 번호**: 340213
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/340213)
# **풀이 날짜** : 2024-11-15

## 문제 
# 문제 설명 :
# 당신은 동영상 재생기를 만들고 있습니다. 당신의 동영상 재생기는 10초 전으로 이동, 10초 후로 이동, 오프닝 건너뛰기 3가지 기능을 지원합니다. 
# 각 기능이 수행하는 작업은 다음과 같습니다.
#
# 동영상의 길이를 나타내는 문자열 video_len, 기능이 수행되기 직전의 재생위치를 나타내는 문자열 pos, 오프닝 시작 시각을 나타내는 문자열 op_start,
# 오프닝이 끝나는 시각을 나타내는 문자열 op_end, 사용자의 입력을 나타내는 1차원 문자열 배열 commands가 매개변수로 주어집니다. 
# 이때 사용자의 입력이 모두 끝난 후 동영상의 위치를 "mm:ss" 형식으로 return 하도록 solution 함수를 완성해 주세요.

## 코드
def solution(video_len, pos, op_start, op_end, commands):
    d = {'next' : 10, 'prev' : -10}
    if op_start <= pos < op_end : pos = op_end
    
    vl = int(video_len.replace(':',''))
    os = int(op_start.replace(':',''))
    oe = int(op_end.replace(':',''))
    p = list(map(int, pos.split(':')))
    
    for comm in commands :
        p[1] += d[comm]
        
        if p[1] < 0 : p[0] -= 1;    p[1] += 60
        elif p[1] >= 60 : p[0] += 1;p[1] -= 60
        
        pms = p[0]*100 + p[1]
        
        if pms < 0 : pms = 0
        elif pms > vl : pms = vl
        if os <= pms < oe : pms = oe
        
        p[0] = pms // 100; p[1] = pms % 100
    
    p[0] = str(p[0]+100); p[1] = str(p[1]+100)
    return p[0][1:] + ':' + p[1][1:]
