a,b=map(int,raw_input().split())
def gcd(p,q):
    s=abs(p-q)
    if (p-q)==0:
        return q
    else:
        return gcd(s,min(p,q))
print gcd(a,b)
