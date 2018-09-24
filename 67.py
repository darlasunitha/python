num=int(raw_input())
if num>0:
    for j in range(2,num):
        if(num%j)==0:
            print "no"
            break
    else:
        print "yes"
