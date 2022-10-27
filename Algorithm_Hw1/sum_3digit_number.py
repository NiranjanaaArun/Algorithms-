def sum_3digit (num):
    sum = 0
    for i in str(num):
        sum=sum+int(i)
    return (sum)

# sum = 0
# while num>0
#   sum = sum + num%10
#   num= num//10
#  return (sum)

number = 653
result = sum_3digit (number)
print(result)