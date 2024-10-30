# ------------------------------------------------------
# 문제 번호 : [2941] 크로아티아 알파벳
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/2941
# 난이도 : X
# 분류 : 구현, 문자열
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
# 다른 알파벳은 한 글자씩 센다.

# 코드
sen = input()
sen = sen.replace('c=','A')
sen = sen.replace('c-','A')
sen = sen.replace('dz=','A')
sen = sen.replace('d-','A')
sen = sen.replace('lj','A')
sen = sen.replace('nj','A')
sen = sen.replace('s=','A')
sen = sen.replace('z=','A')
print(len(sen))
