# 프로그래머스 문제 풀이 - [월간 코드 챌린지 시즌1] 쿼드압축 후 개수 세기 (68936)

## 문제 정보
# **문제 이름**: [월간 코드 챌린지 시즌1] 쿼드압축 후 개수 세기
# **문제 번호**: 68936
# **문제 레벨**: 2
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/68936)
# **풀이 날짜** : 2024-11-28

## 문제 
# 문제 설명 :
# 0과 1로 이루어진 2^n x 2^n 크기의 2차원 정수 배열 arr이 있습니다. 당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.
# 당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
# 만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.
# 그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤, 각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.
# arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때, 배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

## 코드
def quad(arr):
    ret = [0, 0]
    h = len(arr) // 2  
    if h == 0 :
        ret[arr[0][0]] += 1;	return ret
    
    s = sum([sum(x) for x in arr])
    if s == 0 or s == len(arr) ** 2 :
        ret[int(s>0)] += 1;		return ret
    
    q = []
    q.append(quad([row[h:] for row in arr[:h]]))
    q.append(quad([row[:h] for row in arr[:h]]))
    q.append(quad([row[:h] for row in arr[h:]]))
    q.append(quad([row[h:] for row in arr[h:]]))
    q = list(zip(*q))
    
    return [sum(q[0]), sum(q[1])] 

def solution(arr):
    return quad(arr)
