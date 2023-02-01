#write a python program which will read student values such as sno,sname and marks. save the details of  the student in a file by using pickling and read the student record values from the file by using unpickling.impliment this example by using classes and objects.
class Student:
    def __init__(self,name,classs,rollno):
        self.name=name
        self.rollno=classs
        self.classs=rollno
    @staticmethod
    def info(s,name):
     
        print("info",name)
        print("*"*50)
        for i,v in s.__dict__.items():
           
            print(i,v)
        print("*"*50)

s=Student("ayaan",12,54)
s1=Student("kashif",1,5)
s.info(s,"student")
s1.info(s1,"student")

