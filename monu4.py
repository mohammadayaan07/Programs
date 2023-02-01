"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

"""
def check(n):
    dt={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sm=0
    for i in range(len(n)):
        if i>0 and dt[n[i]]>dt[n[i-1]]:
            sm+=dt[n[i]]-2*dt[n[i-1]]
        else:
            sm+=dt[n[i]]
    return sm
n=str(input("enter the roman value:"))
v=n.upper()
print(check(v))