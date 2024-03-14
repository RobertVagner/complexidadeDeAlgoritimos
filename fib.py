def fib(n):
    a,b=0,1
    F=[]
    while (a<n):
        F.append(a)
        a,b=b,a+b
    return F

if __name__=='__main__':
    import sys
    x=int(sys.argv[1])
    print(fib(x))