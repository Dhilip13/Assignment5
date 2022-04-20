class Power:
    def __init__(self,Num,Pow):
        self.Num=Num
        self.Pow=Pow
    def Expon(self):
        print(self.Num**self.Pow)

Obj=Power(10,2)
Obj.Expon()