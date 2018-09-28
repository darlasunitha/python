a,b=map(int,raw_input().split())
s=a*b
for i in range(s+1):
	if (i*i)==s:
		print "yes"
		break
else:
	print "no"
