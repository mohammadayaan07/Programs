"""117. Write a Python program to remove all elements from a given list present in another list.      
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]
Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]"""

def check(list1,list2):
    for i in range(len(list2)):
        if list2[i] in list1:
            list1.remove(list2[i])
                
    return list1
    
    
    
list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2=[2, 4, 6, 8]
print(check(list1,list2))