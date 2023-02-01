"""Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
"""
ls=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,30,20,21]
for v in range(len(ls)):
    if ls[v]%3==0 and ls[v]%5==0:
        ls[v]="fizzbuzz"
    else:
        if ls[v]%5==0:
            ls[v]="buzz"
        elif ls[v]%3==0:
            ls[v]="fizz"
print(ls)