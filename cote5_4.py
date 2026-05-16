'''
숫자의 영역을 반으로 나눠서 힙으로 보관하고
일단 앞쪽에 힙에 넣고
앞쪽힙의 최대값과 뒤쪽힙의 최솟값을 비교하는 방법으로 가야할듯
'''
import sys
import heapq

input = sys.stdin.readline

front_heap = []
back_heap = []

x = int(input())
q = int(input())

# 최대값 찾아야하니 부호 반전
heapq.heappush(front_heap, -x)


for i in range(q):
    a ,b = map(int, input().split())
    
    for num in (a, b):
        # 일단 앞쪽 힙에 넣음
        heapq.heappush(front_heap, -num)
        
        # 앞쪽힙의 최댓값을 빼서 뒷쪽힙으로 넘김
        max_val = -heapq.heappop(front_heap)
        heapq.heappush(back_heap, max_val)
        
        # 균형 맞추기
        if len(front_heap) < len(back_heap):
            min_val = heapq.heappop(back_heap)
            heapq.heappush(front_heap, -min_val)

    print(-front_heap[0])