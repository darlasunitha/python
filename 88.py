p,q=map(int,raw_input().split())
if(p>q):
    min=p
else:
    min=q
while(1):
    if(min%p==0 and min%q==0):
        print(min)
        break
    min=min+1
