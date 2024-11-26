# 프로그래머스 문제 풀이 - 소수 찾기 (42839)

## 문제 정보
# **문제 이름**: 소수 찾기
# **문제 번호**: 42839
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42839)
# **풀이 날짜** : 2024-11-26

## 문제 
# 문제 설명 :
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

## 코드
def is_prime(n):
    if n == 2 : return 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return 0
    return 1

def solution(numbers):
    s = set()
    
    def make_num(n, num) :
        if n == len(numbers) :
            if num == '' : return 0
            num = int(num)
            if num == 0 or num == 1 or num in s: return 0
            s.add(num)
            return is_prime(num)
            
        ret = make_num(n+1, num) + make_num(n+1, numbers[n] + num)
        for i in range(1, len(num)):
            ret += make_num(n+1, num[:i] + numbers[n] + num[i:])
        ret += make_num(n+1, num + numbers[n])
        return ret
    
    return make_num(0, '')
