"""Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
l1=[2,4,3]
l2=[5,6,4]
def sum(n):
    sm=0
    l=len(n)
    for i in range(0,l)[::-1]:
        sm=(sm+n[i])*10
    return sm//10
a=sum(l1)
b=sum(l2)
c=str(a+b)[::-1]
l=[]
for val in c:
    l.append(int(val))
print(l)