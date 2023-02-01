#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx1.py----Instance Data members

class studinfo:pass
s1=studinfo()
s2=studinfo()
print(s1.__dict__)
print(s2.__dict__)
s1.name="ayaan"
s1.roll=45
s1.cls="MCA"
print("After the add element",s1.__dict__)
s2.name="Adil"
s2.roll=144
s2.cls="Qwait"
print("After the adding value in ",s2.__dict__)
