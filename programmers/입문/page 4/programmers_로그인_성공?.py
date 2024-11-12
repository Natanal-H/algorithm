# 프로그래머스 문제 풀이 - 로그인 성공? (120883)

## 문제 정보
# **문제 이름**: 로그인 성공?
# **문제 번호**: 120883
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/120883)
# **풀이 날짜** : 2024-11-12

## 문제 
# 문제 설명 :
# 머쓱이는 프로그래머스에 로그인하려고 합니다. 
# 머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 
# 다음과 같이 로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.
#
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

## 코드
def solution(id_pw, db):
    db = dict(db)
    
    if id_pw[0] in db.keys():
        if id_pw[1] == db[id_pw[0]]:
            return 'login'
        else :
            return 'wrong pw'
    else :
        return 'fail'

## 다른 코드
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"

# := 연산자는 "walrus operator" 또는 "익스프레션 할당" 연산자로 불리며, Python 3.8 이상에서 도입되었습니다. 
# 이 연산자는 변수에 값을 할당하면서 그 값을 바로 사용할 수 있게 해줍니다.
# 즉, 값을 계산하고 그 값을 변수에 저장하면서 동시에 그 값을 다른 곳에서 사용할 수 있게 만들어 주는 연산자입니다.
