liste=[]
kontrol = True
sayi = input("Say�y� girin: ")

for i in range(2,sayi-1,1):
    if sayi % i == 0:
        kontrol = False

if kontrol == True:
    liste.append(i)
    print sayi," asal say�d�r."
else:
    print sayi," asal say� de�ildir."


