liste=[]
kontrol = True
sayi = input("Sayiyi girin: ")
for i in range(2,sayi-1,1):
    if sayi % i == 0:
        kontrol = False
if kontrol == True:
    liste.append(i)
    print sayi," asal sayidir."
else:
    print sayi," asal sayi deðildir."


