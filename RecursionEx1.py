#recursion
def replace(str,a,x):
    if len(str)==0:
        return str
    smalloutput=replace(str[1:],a,x)
    if str[0]==a:
        return x+smalloutput
    else:
        return str[0]+smalloutput
str="ayaan alam"
abc=replace(str,'a','x')
print(abc)
