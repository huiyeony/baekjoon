#2
#1 7 5 8

n = int(input())
s = 2 * n;
w = list(map(int, input().split()))
answer = 200001

w.sort() #정렬 
for i in range(s):
    answer = min(answer, w[s-i-1] + w[i]); #그리디
print(answer);
    
