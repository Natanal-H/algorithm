# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌2] 2개 이하로 다른 비트 (76502)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌2] 2개 이하로 다른 비트
# **문제 번호**: 76502
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/76502)
# **풀이 날짜** : 2024-11-29

## 문제 
# 문제 설명 :
# 양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다. 
# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
#
# 정수들이 담긴 배열 numbers가 매개변수로 주어집니다. 
# numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

## 코드
def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0: answer.append(num + 1)
        else :
            b = (bin(num)[2:])[::-1] + '0'
            for i in range(len(b)-1):
                if b[i:i+2] == '10' :
                    b = (b[:i] + '01' + b[i+2:])[::-1]
                    break
            answer.append(int(b, 2))
            
    return answer
