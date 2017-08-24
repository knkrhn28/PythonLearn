def baklavayap(n):
    s=""
    for i in range(1,n+1):
        for k in range(n-i):
            s=" "+s
        for j in  range((i*2)-1):
            s=s+"*"
        print s
        s=""
    for i in range(n,0,-1):
        for k in range(n-i):
            s=" "+s
        for j in  range((i*2)-1):
            s=s+"*"
        print s
        s=""
baklavayap(int(raw_input("N sayisini Giriniz: ")))
