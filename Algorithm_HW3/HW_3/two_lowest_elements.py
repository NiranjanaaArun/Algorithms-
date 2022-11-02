def lowest_elements(list):
    list.sort(reverse=True)
    return list[-2:]

l=[198,3,4,9,10,9,2]
print(lowest_elements(l))