def recursion(num):
    if num == 0:
        return
    print(num)
    num -= 1
    recursion(num)


recursion(10)