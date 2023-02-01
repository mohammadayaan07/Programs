def tower(n,a,b,c):
    if n==1:
        print("moving last dick",a,"to",c)
        return 
    tower(n-1,a,c,b)
    print("moving ",n," dick",a,"to",c)
    tower(n-1,a,c,b)

ab=tower(3,"x","y","z")
print(ab)
