#이항계수
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
MOD = 1000000007
fac = [1] * (n+1)

for i in range( 1,n+1 ):
    fac[i] = (fac[i-1] * i) % MOD
    
def mod_inverse(a,mod):
    return pow(a , mod-2, mod)
  
def binomial_coefficient(n,k):
    if( k == 1):
        return n;
    elif ( n == k):
        return 1;
    else: # n! / k! (n-k)!
        return (fac[n] * mod_inverse( fac[k] , MOD )* mod_inverse( fac[n-k], MOD )) % MOD;
        

    
print (binomial_coefficient(n,k) )
            
# ( a^ p-2 )mod p == a^-1 mod p       
            
        