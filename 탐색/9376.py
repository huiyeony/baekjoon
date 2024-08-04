# from collections import deque
# cnt = int( input() )
# r ,c = map( int ,input().split() )
# data = []
# for i in range(r):
#     data.append(list( map(int, input().split() ) ))
# prisoner = []
# #탈옥수 위치 찾기 
# for i in range(r):
#     for j in range(c):
#         if(data[r][c] == '$'):
#             prisoner.append( (r,c) )
# delta_x = [ 0,0,-1,1]
# delta_y = [-1,1, 0,0]

# queue = deque()
# visited = [[0 for _ in range(c)] for _ in range(r)] 
# doorCount = 0
# def  BFS(nowY, nowX) :
#     queue.append( (nowY,nowX) )
    
#     while( queue ):
#         nowY, nowX = queue.pop()
        
#         if(visited[nowY][nowX]):
#             continue;
#         visited[nowY][nowX] = 1#방문 처리
#         for i in range( len(delta_x) ):
#             nextY = nowY + delta_y[i]
#             nextX = nowX + delta_x[i]
#             if(data[nextY][nextX] == '*'):
#                 continue;
#             if(visited[nextY][nextX]):
#                 continue;
#             if(data[nextY][nextX] == '#'):
#                 doorCount += 1
#                 data[nextY][nextX] = '.'
#             queue.append( (nowY + delta_y[i], nowX + delta_x[i]) )
        
        
        
        

        