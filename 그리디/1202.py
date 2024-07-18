#보석 도둑
import sys
import heapq
readline = sys.stdin.readline

n , k = map(int, readline().split())
jews = []
bags =[]
temp_jews = []
answer = 0;

for _ in range(n):
    m,v = map( int, readline().split() )
    heapq.heappush( jews, (-v, m))
    


for _ in range(k):
    heapq.heappush( bags, int(readline()) )

#그리디 문제 유형임



print( answer )