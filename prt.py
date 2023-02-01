def check(str,a,b):
    if len(str)==0:
        return str
    if str[0]==a:
        return b+check(str[1:],a,b)
    else:
        return str[0]+check(str[1:],a,b)
str="ayaan"
a=check(str,"a","b")
print(a)