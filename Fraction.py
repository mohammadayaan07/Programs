class fraction:
    def __init__(self,num,deo):
        self.deo=deo
        self.num=num
    def print(self):
        if self.num==0:
            print("0")
        elif self.deo==1:
            print(self.num)
        else:
            print(self.num,"/",self.deo)
    def simplify(self):
        if self.num==0:
            self.deo=1
            return
        current=min(self.num,self.deo)
        while current>1:
            if self.num%current==0 and self.deo%current==0:
                break
            current-=1
        self.num=self.num//current
        self.deo=self.deo//current
        self.print()
    def add(self,f2):
        ad=self.deo*f2.num+f2.deo*self.num
        db=self.deo*f2.deo
        self.num=ad
        self.deo=db
        self.simplify()
        
f=fraction(1,2)
f1=fraction(10,20)
f.simplify()
f1.simplify()
f1.add(f)