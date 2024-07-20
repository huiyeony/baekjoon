n = int(input())
INF = 1e9
data = [INF for _ in range( 3*n )]
data[1] = 0 #초기값
#동적 계획법 문제 
for i in range(1, n):
    
    data[ i*3 ] = min( data[i*3], data[i]+1 )
    data[ i*2 ] = min( data[i*2], data[i]+1 )
    data[ i+1 ] = min( data[i+1], data[i]+1 )
print(data[n])