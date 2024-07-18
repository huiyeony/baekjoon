import sys
from collections import deque
readline = sys.stdin.readline

r , c = map(int, readline().split()) #행과 열 개수

data = [[] for _ in range(r)]
visited = [ [ 0 for _ in range(c) ] for _ in range(r) ]
queue = deque()
#queue.append()
#queue.popleft()
for i in range(r):
    data[i] = list( map( int, readline().split() ) )

#시계방향 회전 
delta_x = [  0,1,0,-1 ]
delta_y = [ -1,0,1, 0 ]

def bfs(y,x):
    # 갈 수 있는 땅 & 방문하지 않은 땅
    area = 0
    if( visited[y][x] ):
        return 0;
    
    queue.append( (y,x) )
    
    while(queue):
        y,x = queue.popleft()
        
        if( data[y][x] == 1 and visited[y][x] == 0 ):
            area += 1;# 면적 1 증가 
            visited[y][x] = 1;
            #주변 육지 탐색 
            for i in range(4):
                newY = y + delta_y[i]
                newX = x + delta_x[i]
                if ( newY < 0 or newY >= r ):#좌표 검사 
                    continue;
                if( newX < 0 or newX >= c ): #좌표 검사
                    continue;
                if( visited[newY][newX] ):#이미 방문
                    continue;
                queue.append( ( newY, newX ))
    return area;

answer = [0,0]


for row in range(r):
    for col in range(c):
        result = bfs(row,col) #연결된 육지 넓이 반환 
        if( result > 0):
            answer[0] += 1
            answer[1] = max(answer[1], result)
            
            
print(answer[0])#섬 개수
print(answer[1])#최대 섬 면적 
