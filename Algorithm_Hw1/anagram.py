def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1)==sorted(s2)

string_1 = "acdes"
string_2 = "scdea"
result = is_anagram(string_1,string_2)
print(result)
