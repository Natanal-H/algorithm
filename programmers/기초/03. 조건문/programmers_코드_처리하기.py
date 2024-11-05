# 프로그래머스 문제 풀이 - 코드 처리하기 (181932)

## 문제 정보
# **문제 이름**: 코드 처리하기
# **문제 번호**: 181932
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181932)

## 문제 
# 문제 설명 :
# 문자열 code가 주어집니다. code를 앞에서부터 읽으면서 만약 문자가 "1"이면 mode를 바꿉니다. 
# mode에 따라 code를 읽어가면서 문자열 ret을 만들어냅니다.
#
# mode가 0일 때
# code[idx]가 "1"이 아니면 idx가 짝수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 0에서 1로 바꿉니다.
# mode가 1일 때
# code[idx]가 "1"이 아니면 idx가 홀수일 때만 ret의 맨 뒤에 code[idx]를 추가합니다.
# code[idx]가 "1"이면 mode를 1에서 0으로 바꿉니다.

## 코드
def solution(code):
    ret = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode + 1) % 2
        elif i % 2 == mode : 
            ret += code[i]          
    
    return 'EMPTY' if len(ret) == 0 else ret
