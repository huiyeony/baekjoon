import sys
from collections import deque
readline = sys.stdin.readline
INF = 1e9
r,c = list( map(int, readline().split()) )
data = [[] for _ in range(r)]
for i in range(r):#갈 수 있는 좌표 
    input = readline().strip()
    data[i] = [ int(char) for char in input ] #붙어있는 문자열 입력 


queue = deque()#큐 
visited = [[0 for _ in range(c)] for _ in range(r)]
delta_x = [ 1,0,-1, 0 ]
delta_y = [ 0,1, 0,-1 ]
distance = [[INF for _ in range(c)] for _ in range(r)]
def BFS( y,x ):
    distance[y][x] = 1;
    queue.append((y,x))
    while (queue):
        y,x = queue.popleft()
        if(visited[y][x] ):
            continue;
        visited[y][x] = 1;#방문 표시
        #도착 여부 확인 
        if( y == r-1 and x == c-1):
            return;
        #옆에 있는 네 방향 칸 확인 
        for i in range( len(delta_x) ):
            nextY = y + delta_y[i];
            nextX = x + delta_x[i];
            if(nextY <0 or nextY >= r):
                continue;
            if(nextX < 0 or nextX >= c):
                continue;
            if(visited[nextY][nextX]):
                continue;
            if(data[nextY][nextX] == 0):
                continue;
            distance[nextY][nextX] = min(distance[nextY][nextX], distance[y][x] + 1); #출발지부터 걸리는 거으리
            queue.append( (nextY,nextX) )
    return;


BFS(0,0)
print(distance[r-1][c-1])
