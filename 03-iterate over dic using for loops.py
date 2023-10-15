#Write a Python program to iterate over dictionaries using for loop

d = {'A':111,'B':222,'C':333,'D':444}
for dict_key, dict_value, in d.items():
    print(dict_key, '_>', dict_value)