def replace(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=="p" and s[1]=="i":
        smalloutput=replace(s[2:])
        return "3.14"+smalloutput
    else:
        smalloutput=replace(s[1:])
        return s[0]+smalloutput
    
a=replace("pikkjpi")
print(a)