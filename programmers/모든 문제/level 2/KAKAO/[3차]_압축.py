# 프로그래머스 문제 풀이 - [2018 KAKAO BLIND RECRUITMENT] [3차] 압축 (17684)

## 문제 정보
# **문제 이름**: [2018 KAKAO BLIND RECRUITMENT] [3차] 압축
# **문제 번호**: 17684
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/17684)
# **풀이 날짜** : 2024-11-25

## 문제 
# 문제 설명 :
# 어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다. LZW 압축은 1983년 발표된 알고리즘으로, 이미지 파일 포맷인 GIF 등 다양한 응용에서 사용되었다.
#
# LZW 압축은 다음 과정을 거친다.
# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.
#
# 주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

## 코드
def solution(msg):
    answer, dic = [], {}
    for i in range(26): dic[chr(ord('A')+i)] = i+1
    
    cache = ''; msg = list(msg)
    while msg : 
        m = msg.pop(0)
        if cache + m not in dic :
            answer.append(dic[cache])
            dic[cache + m] = len(dic) + 1
            cache = m
        else :
            cache += m
    answer.append(dic[cache])
    return answer
