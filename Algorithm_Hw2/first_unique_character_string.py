# return the first unique, if there are no unique characters return "xoxo"

#def first_unique_character(string: str):
#    string=string.lower()
#    for l in string:
#        if string.count(l) == 1:
#            return l

#print(first_unique_character(""))


def unique(string1: str):
    string1=string1.lower()
    d = {}
    for letter in string1: #google
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    print (d)

    for k, v in d.items(): #when we go through a dictionary from above, and try to get values from that, then
        if v==1 :
            return k

    return ""
print(unique("xoxo"))








