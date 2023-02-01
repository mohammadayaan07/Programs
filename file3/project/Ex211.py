lst=[-4, 5, -2, 0, 3, -1, 4, 9]
def sms(lst):
    for v  in range(len(lst)):
        for i in range(v):
            if lst[i]>lst[i+1]:
                rmd=lst[i+1]
                lst[i+1]=lst[i]
                lst[i]=rmd
    return lst[0]+lst[1]
print(sms(lst))