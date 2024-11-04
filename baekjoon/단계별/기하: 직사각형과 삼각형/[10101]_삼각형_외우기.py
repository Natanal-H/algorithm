# ------------------------------------------------------
# 문제 번호 : [10101] 삼각형 외우기
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/10101
# 난이도 : X
# 분류 : 구현, 기하학
# 날짜 : 2024-11-04
# ------------------------------------------------------

# 문제 설명 :
# 삼각형의 세 각을 입력받은 다음,
# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

# 코드
a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180 :
    print('Error')
elif a == b and b == c :
    print('Equilateral')
elif a == b or b == c or a == c :
    print('Isosceles')
else :
    print('Scalene')
