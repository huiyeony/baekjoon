p = int(input())
ch = 1000 - p;
coins = [500,100,50,10,5,1]
answer = 0;
for c in coins:
    answer += ch//c;
    ch %= c;
    if(ch == 0):
        break;
print(answer)