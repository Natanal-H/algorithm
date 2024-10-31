# ------------------------------------------------------
# 문제 번호 : [9506] 약수들의 합
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/9506
# 난이도 : X
# 분류 : 수학, 구현, 정수론
# 날짜 : 2024-10-31
# ------------------------------------------------------

# 문제 설명 :
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

# 코드
while True :
    n = int(input())
    
    if n == -1 : break

    arr = [1]
    i = 2

    while i ** 2 <= n :
        if n % i == 0 :
            arr.append(i)
            
            if i**2 != n :
                arr.append(n // i)
        i += 1
        
    arr.sort()
    if n == sum(arr):
        print(f"{n} = {' + '.join(map(str, arr))}")
    else :
        print(f"{n} is NOT perfect.")
