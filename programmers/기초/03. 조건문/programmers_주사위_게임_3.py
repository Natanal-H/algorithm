# 프로그래머스 문제 풀이 - 주사위 게임 3 (181916)

## 문제 정보
# **문제 이름**: 주사위 게임 3
# **문제 번호**: 181916
# **링크**: [링크](https://programmers.co.kr/learn/courses/30/lessons/181916)
# **풀이 날짜** : 2024-11-06

## 문제 
# 문제 설명 :
# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

## 코드
def solution(a, b, c, d):
    nums = sorted([a, b, c, d])
    counts = [nums.count(n) for n in nums]
    
    if max(counts) == 4:
        return a * 1111
    
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    
    elif max(counts) == 2:
        if min(counts) == 2:
            return (nums[2] + nums[0]) * abs(nums[2] - nums[0])
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)
