class sinifPolinom():
    def __init__(self,poly,x):
        self.poly=poly
        self.x=x
        self.sonuc=0
        self.fonksiyonPolinom()
    def fonksiyonPolinom(self):
        for i in range(len(self.poly)):
            self.sonuc+=self.poly[i]*self.x**i
        print self.sonuc
poly=(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
sonuc=0
yazdir=sinifPolinom(poly,x)
