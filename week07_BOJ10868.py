import sys
import math
input = sys.stdin.readline

N,M = map(int, input().split())
A = [int(input()) for _ in range(N)]

block_size = int(math.sqrt(N)) + 1 # 블럭의 크기 N의 2루트 값으로 함, 이게 가장 빠름
num_blocks = math.ceil(N / block_size) # 올림을 통해 블럭의 개수를 구함

# 각 블록의 최솟값 저장할 리스트, 초기는 무한대 값
block_min = [float('inf')] * num_blocks

for i in range(N):
    b = i//block_size # 현재 확인 중인 자리가 어디 블록인지 탐색
    if A[i] < block_min[b]: # 만약 그 값이 해당하는 블록의 최솟값 보다 작으면
        block_min[b] = A[i] # 새로 없데이트

result = []

for _ in range(M):
    a, b = map(int, input().split())
    # a, b -1를 통해 인덱스로 전환
    a -= 1
    b -= 1
    
    answer = float('inf') # 초기값을 무한대값
    
    # 해당 범위의 첫번째 블록과 마지막 블록의 번호를 추출
    start_block = a//block_size
    end_block = b//block_size    
    
    # 같은 블록안에 해당되는 경우 직접확인
    if start_block == end_block:
        for i in range(a, b+1): # 직접 다 확인하며
            if A[i] < answer: # 만약 최솟값 보다 작으면
                answer = A[i] # 갱신
            
    else:
        # 왼쪽 블록(첫번째)에서 최솟값 탐색
        for i in range (a, (start_block+1)*block_size):
            if A[i] < answer:
                answer = A[i]
        # 중간 블록들 중에서 최솟값 탐색
        for i in range(start_block + 1, end_block):
            if block_min[i] < answer:
                answer = block_min[i]
        # 오른쪽 블록(마지막)에서 최솟값 탐색
        for i in range(end_block*block_size, b+1):
            if A[i] < answer:
                answer = A[i]
    result.append(str(answer))

print('\n'.join(result))

