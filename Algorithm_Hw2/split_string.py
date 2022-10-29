test_str = "aaaaacddddd"
res_first = test_str[0:len(test_str)//2]
res_second = test_str[len(test_str)//2
        if len(test_str)%2 == 0
        else ((len(test_str)//2)+1):]

print("The first part of string : " + res_first)
print("The second part of string : " + res_second)

complete_str = res_second+res_first

if len(test_str) % 2 == 0:
    print("The complete string :", f'{res_second}'+'c'+f'{res_first}')
else:
    print("The complete string :", f'{res_second}{res_first}'+'c')






