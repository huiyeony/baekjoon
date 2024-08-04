n, k = map(int, input().split())
data = []
for _ in range(n):
    w,v = map(int, input().split())
    data.append( [w,v] )
data.insert(0, (0,0))

dp = [[0]* (k+1) for _ in range(n+1) ]
#무게가 k 일때 최대 효용
for i in range( 1, n+1 ):
    for j in range( 1, k+1 ):
        if(data[i][0] <= j):
            dp[i][j] = max( dp[i-1][j], data[i][1] + dp[i-1][j - data[i][0]])
        else:
            dp[i][j] = dp[i-1][j]

print( dp[n][k] )
