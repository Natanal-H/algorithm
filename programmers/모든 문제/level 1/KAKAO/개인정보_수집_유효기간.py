# 프로그래머스 문제 풀이 - [2023 KAKAO BLIND RECRUITMENT] 개인정보 수집 유효기간 (150370)

## 문제 정보
# **문제 이름**: [2023 KAKAO BLIND RECRUITMENT] 개인정보 수집 유효기간
# **문제 번호**: 150370
# **문제 레벨**: 1
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/150370)
# **풀이 날짜** : 2024-11-14

## 문제 
# 문제 설명 :
# 고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 
# 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.
#
# 오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다. 
# 이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

## 코드
def solution(today, terms, privacies):
    dt = {}
    result = []
    for term in terms :
        s = term.split()
        dt[s[0]] = int(s[1])
        
    for i, p in enumerate(privacies):
        data = p.split()
        date = [int(x) for x in data[0].split(".")]
        date[1] += dt[data[1]]
        while date[1] > 12 :
            date[0] += 1
            date[1] -= 12
        
        for i in range(3):
            if date[i] < 10:
                date[i] = '0' + str(date[i])
            else :
                date[i] = str(date[i])
                
        result.append('.'.join(date))
        
    return [i+1 for i,v in enumerate(result) if today >= v]
