# 프로그래머스 문제 풀이 - [2019 KAKAO BLIND RECRUITMENT] 오픈채팅방 (42888)

## 문제 정보
# **문제 이름**: [2019 KAKAO BLIND RECRUITMENT] 오픈채팅방
# **문제 번호**: 42888
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/42888)
# **풀이 날짜** : 2024-11-27

## 문제 
# 문제 설명 :
# 카카오톡 오픈채팅방에서는 친구가 아닌 사람들과 대화를 할 수 있는데, 본래 닉네임이 아닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.
# 신입사원인 김크루는 카카오톡 오픈 채팅방을 개설한 사람을 위해, 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다. 채팅방에 누군가 들어오면 다음 메시지가 출력된다.
# "[닉네임]님이 들어왔습니다."
# 채팅방에서 누군가 나가면 다음 메시지가 출력된다.
# "[닉네임]님이 나갔습니다."
#
# 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다.
# 닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
#
# 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때, 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.

## 코드
def to_string(b, s):
    if b : return s + "님이 나갔습니다."
    else : return s + "님이 들어왔습니다."

def solution(record):
    arr, d = [], {}
    
    for r in record :
        s = r.split();
        if s[0] != 'Change' :
            arr.append([len(s)==2, s[1]])
        if len(s) == 3:
            d[s[1]] = s[2]
            
    return [to_string(a[0], d[a[1]]) for a in arr]
