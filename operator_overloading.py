class Complex:
    def __init__(self,a,b):
        self.real=a
        self.comp=b
    def __add__(self, other):
        return Complex(self.real+other.real,self.comp+other.comp)
    def __str__(self):
        return str(self.real)+" + "+str(self.comp)+"j"

a=Complex(1,1)
b=Complex(2,2)
print(str(a+b))