def sum_list(list):

    total = sum(list)
    mean = total/len(list)
    return mean


n= [1,3,5,6,4,10,2,3]
print(sum_list(n))
del n[2:4]
del n[-3]
print(n)


