# 프로그래머스 문제 풀이 - [2020 KAKAO BLIND RECRUITMENT] 문자열 압축 (60057)

## 문제 정보
# **문제 이름**: [2020 KAKAO BLIND RECRUITMENT] 문자열 압축
# **문제 번호**: 60057
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/60057)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

## 코드
def cnt(n) :
    return len(str(n+1)) if n > 0 else 0

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2 + 1):
        l, a, c = i, s[:i], 0
        for j in range(i, len(s), i):
            if j + i > len(s) : l += cnt(c) + len(s) - j; c = 0; break
                        
            if a == s[j:j+i] : c += 1
            else :
                l += cnt(c) + i 
                c = 0
                a = s[j:j+i]
        
        l += cnt(c)
        answer = min(answer, l)
    
    return answer
