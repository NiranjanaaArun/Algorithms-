def leap_year(num):
    if num%4 == 0:
        if num%100 == 0:
            if num%400==0:
                print(f'{num} is a leap year')
            else:
                print(f'{num} is not a leap year')
        else:
            print(f'{num} is a leap year')
    else:
        print(f'{num} is not a leap year')

leap_year(2017)
leap_year(1900)
leap_year(2012)
leap_year(2000)