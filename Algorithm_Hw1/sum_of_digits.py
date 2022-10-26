def sum_of_digits(n):
    odds = 0
    even = 0
    while n > 0:
        current_digit = n % 10
        if current_digit % 2:
            odds = odds + 1
        else:
            even = even + 1
        n = n//10
    return [odds, even]

test_n = 13454698
result = sum_of_digits(test_n)
print(result)

