liste=[]
kontrol = True
sayi = input("Sayýyý girin: ")

for i in range(2,sayi-1,1):
    if sayi % i == 0:
        kontrol = False

if kontrol == True:
    liste.append(i)
    print sayi," asal sayýdýr."
else:
    print sayi," asal sayý deðildir."


