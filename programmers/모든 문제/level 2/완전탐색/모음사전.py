# 프로그래머스 문제 풀이 - 모음사전 (84512)

## 문제 정보
# **문제 이름**: 모음사전
# **문제 번호**: 84512
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/84512)
# **풀이 날짜** : 2024-12-17

## 문제 
# 문제 설명 :
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 
# 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.
# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

## 코드
count = 0

def solution(word):
    aeiou = ['A','E','I','O','U']    
    
    def dfs(s):    
        global count
        count += 1
        
        if s == word: return True
        if len(s) == 5: return False        
        
        for a in aeiou:
            tf = dfs(s+a)
            if tf : return True
    
    dfs('')
    
    return count-1
