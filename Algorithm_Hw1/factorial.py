def factorial(n):
    n>0
    fac=1
    for i in range(1,n+1):
        fac=fac*n
        n=n-1
    return(fac)

num = 3
fact= factorial(num)
print(fact)
