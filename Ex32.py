#Write a Python program to generate all sublists of a list. 
def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1): #4--0,1,2,3
        for j in range(i): #0  0,1  0,1,2    0,1,2,3
            lists.append(l[j: i]) #l[0:0] l[0:1]l[1:1] l[0:2]l[1:2]l[2:2] l[0:3][1:3][2:3][3:3]
    return lists
 
# driver code
l1 = [1, 22, 3]
print(sub_lists(l1))