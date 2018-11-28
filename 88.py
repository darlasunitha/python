n,m=map(int,raw_input().split())
if(n>m):
    min1=n
else:
    min1=m
while(1):
    if(min1%n==0 and min1%m==0):
        print(min1)
        break
    min1=min1+1
