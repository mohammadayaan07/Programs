#5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
	#	Sample List : ['abc', 'xyz', 'aba', '1221']
	#	Expected Result : 2
SampleList=['abc', 'xyz', 'aba', '1221']
def lst(SampleList):
    for val in SampleList:
        e=str(val)
        if e[0]== e[len(e)-1]:
            print(e)
        
lst(SampleList)