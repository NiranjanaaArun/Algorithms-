def word(str1):
    a = set(str1)
    if len(str1)>len(a):
        print(False)
    elif len(str1)<len(a):
        print(False)
    else:
        print(True)



string = "goose"
result = word(string)
print(result)








