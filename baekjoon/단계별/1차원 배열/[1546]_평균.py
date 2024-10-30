# ------------------------------------------------------
# 문제 번호 : [1546] 평균
# 플랫폼 : Baekjoon
# 링크 : https://www.acmicpc.net/problem/1546
# 난이도 : X
# 분류 : 수학, 사칙연산
# 날짜 : 2024-10-30
# ------------------------------------------------------

# 문제 설명 :
# 점수 중에 최댓값을 골라 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# 코드
N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

for i in range(N):
    scores[i] *= 100 / max_score
    
print(sum(scores)/N)
