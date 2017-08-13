# -*- coding: cp1254 -*-
def turevHesapla(poly):
    sonuc = ()
    for i in range(0, len(poly)):
        if poly[i] != 0.0:
            sonuc += (poly[i]*(i),)
        else:
            continue 
    return sonuc
poly = (13.39, 0.0, 17.5, 3.0, 1.0)
print turevHesapla(poly)

