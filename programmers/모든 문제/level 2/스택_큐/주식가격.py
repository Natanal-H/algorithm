# 프로그래머스 문제 풀이 - 주식가격 (42584)

## 문제 정보
# **문제 이름**: 주식가격
# **문제 번호**: 42584
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42584)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

## 코드
def solution(prices):
    l = len(prices)
    answer = [0] * l
    
    for i in range(l-2,-1,-1) :
        cnt = 0
        for j in range(i+1,l) :
            cnt += 1
            if prices[i] > prices[j] : break
            elif prices[i] == prices[j] :
                cnt += answer[j]
                break
        answer[i] = cnt
        
    return answer
