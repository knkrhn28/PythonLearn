son=int(raw_input("ust Sinir: "))
liste=[]
for i in range(2,son):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        liste.append(i)
print liste
            
