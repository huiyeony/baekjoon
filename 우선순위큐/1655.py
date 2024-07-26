import heapq
import sys
input = sys.stdin.readline
#5 1 2 3
leftHeap = []#최대힙
rightHeap = []#최소힙 
answer = []
n = int( input() )
for i in range(n):
    num = int( input() )
    if( len(leftHeap) == len(rightHeap) ):
        heapq.heappush( leftHeap, -num )
    elif( len(leftHeap) > len(rightHeap) ):
        heapq.heappush( rightHeap, num )
    if( rightHeap and -leftHeap[0] > rightHeap[0] ):
        l_value = -heapq.heappop( leftHeap )
        r_value = heapq.heappop( rightHeap )
        
        heapq.heappush( leftHeap, -r_value )
        heapq.heappush( rightHeap, l_value )
    answer.append( -leftHeap[0] )
        
print(" -------- ")
for i in range(n):
    print(answer[i])
