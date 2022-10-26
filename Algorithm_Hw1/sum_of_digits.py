def sum_digits(num):
    a = 0
    sum = 0
    while( a < num+1):
        sum+=a
        a+=1
    return (sum)

total_of = 8
final_result = sum_digits(total_of)
print(final_result)


