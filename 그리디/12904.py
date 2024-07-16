#첫째 줄에 s, 둘째 줄에 t가 주어진다
# s 문자열 뒤에 A 추가함
# s를 뒤집고 문자열 뒤에 B를 추가함
#s 를 t 로 바꿀 수 있으면 1, 없으면 0 출력



s = input()
t = input()

answer = 0;

while( len(s) < len(t) ):
    if(t[-1] == 'A'):
       t = t[:-1];
    
    else:
        t = t[:-1];
        t = t[::-1];
   
if(t == s):
    print(1)
else:
    print(0)

        
