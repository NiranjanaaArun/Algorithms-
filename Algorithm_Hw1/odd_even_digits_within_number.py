def odd_even_digit(a):
    c=a
    b=0
    while b == a%10:
        if b % 2 == 0:
            print (b, "is a even number")
        elif b % 2 != 0:
            print(b, "is an odd number")
        else:
            break
    c= c//10

number = 514235713
odd_even_digit(number)
print (c)
















