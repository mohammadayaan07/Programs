
def check(a1,a2,a3):
    cnt=0
    ls=[a1,a2,a3]
    l=[]
    for a in ls:
        for i in range(1,a+1):
            if a%i==0:
                cnt=cnt+1
        if cnt>2:
            l.append("yes")
        else:
            l.append("no")
    c=0
    for val in l:
        if val=="yes":
            c=c+1
    if c>1:
        return "yes"
    else:
        return "no"
        
a1,a2,a3=23,32,12
print(check(a1,a2,a3))
