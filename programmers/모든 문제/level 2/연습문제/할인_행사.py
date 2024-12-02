# 프로그래머스 문제 풀이 - 할인 행사 (131127)

## 문제 정보
# **문제 이름**: 할인 행사
# **문제 번호**: 131127
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/131127)
# **풀이 날짜** : 2024-12-02

## 문제 
# 문제 설명 :
# XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다. XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 
# 할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.
#
# 정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, 
# XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

## 코드
def solution(want, number, discount):
    answer, dj, dm = 0, {}, {}
    
    for i in range(len(want)): 
        dj[want[i]] = number[i]
        dm[want[i]] = 0
    
    def check():
        for k in dj.keys():
            if dm[k] != dj[k]: return 0
        return 1
    
    for i in range(len(discount)):
        if i > 9 : dm[discount[i-10]] -= 1
        if discount[i] in dm : dm[discount[i]] += 1
        else : dm[discount[i]] = 1
        answer += check();  
        
    return answer
