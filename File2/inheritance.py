class Father:
    def __init__(self):
        self.name=input("inter the name of Father ")
        self.fproperties=float(input("Enter the father properties"))
class Son(Father):
    def __init__(self):
        self.name=input("inter the name of son ")
        self.sproperties=float(input("Enter the son properties"))
        Father.__init__(self)

        
    def info(self):
        print("\tFATHER")
        print(self.name)
        print(self.fproperties)
        print("\tson")
        print(self.name)
        print(self.sproperties)
        print("total Properties:",self.sproperties+self.fproperties)

S=Son()
S.info()

        
        