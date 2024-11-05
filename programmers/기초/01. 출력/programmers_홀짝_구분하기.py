# 프로그래머스 문제 풀이 - 홀짝 구분하기 (181944)

## 문제 정보
# **문제 이름**: 홀짝 구분하기
# **문제 번호**: 181944
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181944)

## 문제 
# 문제 설명 :
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 
# 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

## 코드
a = int(input())
print(f"{a} is {'odd' if a%2 else 'even'}")
