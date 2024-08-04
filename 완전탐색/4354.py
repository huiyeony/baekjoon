import sys
readline = sys.stdin.readline

def failure_function(str):
    
    n = len(str)
    table = [0] * n
    j =0
    for i in range(1, n):
        if(j > 0 and str[j]!= str[i]):
            j = 0
        if(str[j] == str[i]):
            j += 1
            table[i] = j

    if( n % ( n - table[-1] ) != 0):
        print(1)
    else :
        print ( n // ( n - table[-1]) )#거듭제곱의 지수 부분 

while( True ):
    str = readline().strip()#\n 개행문자 삭제
    if(str == '.'):
        break;
    failure_function(str)