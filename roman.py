def romandigit():
    n=int(input("enter a number"))
    val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sym=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    roman=""
    i=0
    while n>0:
        div =n//val[i]
        n=n%val[i]
        while div:
            roman=roman +sym[i]
            div=div-1
        i=i+1
    return roman 
print(romandigit())