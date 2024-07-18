import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))

data.insert(0,0)
answer = 0

#예상 등수대로 정렬
data.sort()
    
for i in range(N):
    if(i != data[i]):
        answer += abs(i-data[i])
         
#출력   
print(answer)

        
        
     
        
    
    