
s = input()
p = input()

s = '0' + s
p = '0' + p

start_index = 1;
end_index = 2;
count = 0;
while(end_index <= len(p) ):
    if(p[ start_index : end_index ] in s):
        end_index += 1;
    else:
        start_index = end_index - 1; #시작 인덱스 초기화
        count += 1;
    
count += 1; #마지막 문자열이 포함된 부분 문자열
print(count)