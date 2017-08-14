def ebob(a,b):
    while b:
        a,b=b,a%b;
    return a;
print ebob(56,44)
