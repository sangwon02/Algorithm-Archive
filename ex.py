i = 0
li = []
set_data = set() # 세트 선언

# 이게 더 빠름 이거 쓰는 습관 들이기
import sys
input = sys.stdin.readline

n =int(input().rstrip())

n = int(input())
s = input().strip()  # 문자열 받을때
n, m = map(int, input().split())

#리스트 요소 하나하나 띄어쓰기 출력
print(" ".join(map(str, li)))

from itertools import combinations

map = [list(map(int, input().split())) for _ in range(n)]
    
n = int(input())

str1 = input()

n1, n2 = map(int, input().split())

print(i, end ="")

print(*li)  # 리스트 뛰어쓰기하며 출력

li.append(int(input())) #for문으로 입력 받을때

# 주의 sys.stdin.readline 쓰면 안됨
li.append(list(map(int, input()))) # 띄어쓰기 없이 입력 받아도 정수 하나씩 저장

li = list(map(int, input().split()))

set1 = set(map(int, input().split())) # 집합 중복된 값 제거하고 리스트보다 빠름

li = input().split() # 문자열 띄어쓰기 별로 나누어서 저장

print("dfsfsdfsdfsdf"[:3])
#3번째 까지 문자열 출력

li.sort(reverse=False)
#숫자, 문자 오름차순으로 정렬

li.sort(reverse=True)
#숫자, 문자 내림차순으로 정렬

li.sort(key=len) 
# 문자열 길이순으로 정렬

li.sort(key=lambda x:x[0])
# 2차원 리스트 첫 번째 값을 기준으로 오름차순 이 때, x 값에 -를 취해주면 내림차순 정렬을 할 수 있다.

del li[0] 
#리스트 첫번째 값 제거

min(li), max(li)
#가장 작은 값과 큰 값 출력

li =[]
k = 0

num = 0
while num <= 100:
    print(num)
    num = num + 1
    
print(*li) # 리스트 대괄호 없이 출력

array = list(range(1,n+1)) # 1부터 n까지의 리스트 생성

li.append(k)
#리스트에 항목추가
for i in range(n):
    li.append(int(input()))

li = ['A', 'B', 'C', 'D', 'B', 'D', 'E']
st = set(li) #집합set으로 변환
li = list(st) #list로 변환

arr = [[0] * 100 for _ in range(100)] # 배열 만들기


# LCS(Longest Common Subsequence, 최장 공통 부분 수열)는 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 알고리즘
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    # DP 테이블 초기화 (0으로 채워진 2차원 리스트)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:  # 문자가 같으면
                dp[i][j] = dp[i-1][j-1] + 1
            else:  # 문자가 다르면
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

string_a = "ACAYKP"
string_b = "CAPCAK"
print(f"LCS의 길이: {lcs(string_a, string_b)}")

