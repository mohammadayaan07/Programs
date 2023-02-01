def sorted(ls):
    l=len(ls)
    for i in range(0, l):   
        for j in range(0, l-i-1): 
            if (ls[j][-1] > ls[j + 1][-1]): 
                temp = ls[j] 
                ls[j]= ls[j + 1] 
                ls[j + 1]= temp 
                print(ls)
    return ls
ls=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(ls))