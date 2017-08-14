def ebob(a,b):
    while b:
        a,b=b,a%b;
    return a;
def ekok(a,b):
    return a*b/ebob(a,b)

print ekok(56,44)
