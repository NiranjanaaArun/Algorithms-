def sum_and_mult(arr):
    sum_result=0
    mult_result=1

    for i in arr:
        sum_result += i
        mult_result *= i

    return [sum_result, mult_result]

test_list= [1, 7, 3]
result_list=sum_and_mult(test_list)
print(test_list)
print("Sum: " + str(result_list[0]))
print("Multiplication: " + str(result_list[1]))
