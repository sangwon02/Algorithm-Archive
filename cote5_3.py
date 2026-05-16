'''
첫 알파벳부터 하나씩 탐색하고
그게 C이면 앞에 있는 숫자와 뒤에 남아있는 숫자를 비교해서
낮은 값을
최종값에 더해주면 될듯
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
result = 0

for i in range(len(s)):
    if s[i] == "C":
        left = i
        right = len(s) - 1 - i
        
        result += min(left, right) + 1
        

print(result)
