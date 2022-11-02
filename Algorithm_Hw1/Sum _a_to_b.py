#def numbers(a,b): #a= 3, b =5
#    sum = 0
#    while a>=0:
#        sum= sum+a
#        a= a+1
#        if int(a) == int(b+1):
#            return sum

#print(numbers(3,5))


def numbers(a,b): #a= 3, b =5
    sum = 0
    for i in range (a,b+1):
        sum= sum+i
        i += 1
    return sum
print(numbers(3,5))