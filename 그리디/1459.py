#그리디 문제

r, c, w, s = map(int, input().split())


answer = 0
move = min( r,c )
dif = abs( r-c )
if( 2*w > s):
    answer += s * move
    if( w < s):
        answer += dif * w
    else:
        answer += (dif//2) *  2*s + (dif%2) * w
else:
    answer += ( r+c ) * w

print(answer)