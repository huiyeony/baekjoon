# import sys
# from collections import deque
# readline = sys.stdin.readline;


# c,r = map(int, readline().split())
# queue = deque()
# data = []
# visited = []
# for _ in range(r):
#     data.append( list(map(int, readline().split()) ))
#     visited.append( [0 for _ in range(c)] )
    
# delta_y = [-1, 0, 1,  0]
# delta_x = [ 0, 1, 0, -1]

# def BFS( y,x ):
#         queue.append( (y,x) )

#         while(queue):
#             nowY, nowX = queue.popleft()
#             for i in range( len(delta_x) ):
#                 nextY = nowY + delta_y[i]
#                 nextX = nowX + delta_x[i]
#                 if(nextY <0 or nextY >= r):
#                     continue;
#                 if(nextX < 0 or nextX >=c):
#                     continue;
#                 if( data[nextY][nextX] != 0): #안 익은 토마토 
#                     continue;
#                 data[nextY][nextX] = data[nowY][nowX] + 1; # 하루뒤 익은 토마토
#                 queue.append( (nextY, nextX) )
            
         
    