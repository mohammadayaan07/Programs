class fraction():
    def __init__(self):
        self.num=int(input("enter the num"))
        self.den=int(input("enter the num"))
    def ptr(self):
        print(self.num,"/",self.den)
    def simplfy(self):
        current=min(self.num,self.den)
        while current>1:
            if self.num%current==0 and self.den%current==0:
                break
            else:
                current -=1
        self.num=self.num//current
        self.den=self.den//current
f=fraction()
f.ptr()
f.simplfy()
f.ptr()