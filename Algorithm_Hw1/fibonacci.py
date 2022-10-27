def fibonacci(num):
    a=0
    b=1
    print("Fibonacci Series:", a , b , end=" ")
    for i in range(0,num+1):
        c=a+b
        a=b
        b=c
        print(c , end=" ")

n= 10
result = fibonacci(n)
print(result)
