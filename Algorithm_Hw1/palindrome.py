def palindrome (str1):
    rev_str = reversed(str1)


    if list(str1) == list(rev_str):
        print ("the string is a palindrome")
    else:
        print("The string is not a palindrome")

#return str1[::-1]== str1


#def is _palindrome(s):
#    for i in range (len(s)):
#        t = s[:i] + s[i + 1:]
#           print (t)
#        if t == t[::1]:
#            return True

#   return False


string1 = "rtdar"
string2 = "radar"
print(palindrome(string1))
print(palindrome(string2))

