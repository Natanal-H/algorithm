# ------------------------------------------------------
# 문제 번호 : [2745] 진법 변환
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2745
# 난이도 : X
# 분류 : 수학, 구현, 문자열
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

# 코드
N, B = input().split()
result = 0

B = int(B)
reversed_N = N[::-1]

for i in range(len(N)):
    if reversed_N[i] >= 'A' :
        result += (ord(reversed_N[i]) - ord('A') + 10) * (B ** i)
    else :
        result += int(reversed_N[i]) * (B ** i)

print(result)
