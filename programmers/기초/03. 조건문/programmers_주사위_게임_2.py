# 프로그래머스 문제 풀이 - 주사위 게임 2 (181930)

## 문제 정보
# **문제 이름**: 주사위 게임 2
# **문제 번호**: 181930
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181930)

## 문제 
# 문제 설명 :
# 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 
# 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a^2 + b^2 + c^2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a^2 + b^2 + c^2 ) × (a^3 + b^3 + c^3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

## 코드
def score(arg, pow):
    ans = 1
    for i in range(1, pow+1):
        ans *= sum([n**i for n in arg])
    return ans
        
def solution(a, b, c):
    arr = sorted([a, b, c])
    
    if arr[0] == arr[2] : 
        return score(arr,3)
    if arr[0] == arr[1] or arr[1] == arr[2] :
        return score(arr,2) 
    return score(arr,1)
