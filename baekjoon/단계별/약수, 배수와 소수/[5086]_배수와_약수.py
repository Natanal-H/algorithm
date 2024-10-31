# ------------------------------------------------------
# 문제 번호 : [5086] 배수와 약수
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/5086
# 난이도 : X
# 분류 : 수학, 사칙연산
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
#
# 첫 번째 숫자가 두 번째 숫자의 약수이다. => factor
# 첫 번째 숫자가 두 번째 숫자의 배수이다. => multiple
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. => neither

# 코드
while True :
    A, B = map(int, input().split())
    
    if A == B and A == 0 : break
    
    if B // A > 0 and B % A == 0 :
        print('factor')
    elif A // B > 0 and A % B == 0 :
        print('multiple')
    else :
        print('neither')
