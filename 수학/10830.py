#행렬의 제곱
import sys
input = sys.stdin.readline

n , k = map( int, input().split() )
m = []
for _ in range(n):
    m.append(list( map( int, input().split() )) )

def multiply_matrix( A, B ):
    row_A = len(A)
    col_A = len(A[0])
    col_B = len(B[0])
    
    matrix = [ [0] * row_A for _ in range(col_B) ]
    for i in range(row_A):
        for j in range(col_B):
            answer = 0
            for k in range(col_A):
                answer += ( A[i][k] * B[k][j] ) 
            matrix[i][j] = (answer%1000)
    return matrix

#분할 정복 
def pow_matrix(m,b):
    if(b == 1):
        return m
    
    elif( b % 2 == 0):
        temp = pow_matrix( m , b//2 )
        return multiply_matrix(temp, temp)
    else:
        temp = pow_matrix( m , b//2 )
        return multiply_matrix( m, multiply_matrix( temp, temp ))
    
                
A = pow_matrix(m,k)
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
