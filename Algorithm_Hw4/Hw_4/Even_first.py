def even_first(arr):
    evens = []
    odds = []

    for value in arr:
        if value % 2 == 0:
            evens.append(value)
        else:
            odds.append(value)
    combined = evens + odds

    return combined

test_list = [7, 3, 5, 6, 4, 10, 3, 2]
result = even_first(test_list)
print(result)