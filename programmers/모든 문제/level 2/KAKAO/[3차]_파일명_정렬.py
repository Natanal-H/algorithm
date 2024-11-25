# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [3차] 파일명 정렬 (17686)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [3차] 파일명 정렬
# **문제 번호**: 17686
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17686)
# **풀이 날짜** : 2024-11-25

## 문제 
# 문제 설명 :
# 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.
# HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
# NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
# TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.
#
# 파일명을 세 부분으로 나눈 후, 다음 기준에 따라 파일명을 정렬한다.
# 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 이때, 문자열 비교 시 대소문자 구분을 하지 않는다. 
# 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
# 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다. 

## 코드
def slicing(s) :
    start, end = 0, 0
    for i in range(len(s)):
        if '0' <= s[i] <= '9' : start = i; break
    for i in range(start+1, len(s)):
        if not ('0' <= s[i] <= '9') : end = i; break
    if end == 0 or end - start > 5 : end = start + 5
    return [s[:start], s[start:end], s[end:]]

def solution(files):
    answer = []
    for i, f in enumerate(files): answer.append([i] + slicing(f))
    answer.sort(key=lambda x: (x[1].lower(), int(x[2]), x[0]))
    return [a[1]+a[2]+a[3] if a[3] else a[1]+a[2] for a in answer]
